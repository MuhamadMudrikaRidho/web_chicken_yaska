from flask import Blueprint, render_template, current_app, request, session, redirect, url_for, jsonify
from bson import ObjectId

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.before_request
def restrict_to_admins():
    
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    if not session.get('isAdmin', False):
        return redirect('/')

@admin_bp.context_processor
def inject_admin_data():
    db = current_app.config['DB']
    user = session.get('username')
    admin = db.users.find_one({"username": user}) if user else None
    return {'admin': admin}

def convert_ids_to_strings(document):
    if isinstance(document, list):
        return [convert_ids_to_strings(item) for item in document]
    elif isinstance(document, dict):
        return {
            key: str(value) if isinstance(value, ObjectId) else convert_ids_to_strings(value)
            for key, value in document.items()
        }
    else:
        return document
    
@admin_bp.route("/")
def dashboard():
    db = current_app.config['DB']
    
    total_users = db.users.count_documents({})
    total_menu = db.menu.count_documents({})
    
    pipeline = [
        {"$match": {"status": "selesai"}},
        {"$group": {
            "_id": None,
            "total_omzet": {"$sum": "$total_price"},
            "total_orders": {"$sum": 1}
        }}
    ]
    
    aggregation_result = list(db.orders.aggregate(pipeline))
    
    total_omzet = aggregation_result[0]['total_omzet'] if aggregation_result else 0
    total_orders = aggregation_result[0]['total_orders'] if aggregation_result else 0
    
    return render_template(
        'admin/index.html',
        total_orders=total_orders,
        total_users=total_users,
        total_omzet=total_omzet,
        total_menu=total_menu
    )


@admin_bp.route('/menu', methods=["GET", "POST"])
def menu() :
    if request.method == "POST":
        return jsonify({"status" : "success"})
    
    db = current_app.config['DB']
    menus = list(db.menu.find({}))
    
    for menu in menus :
        menu["_id"] = str(menu["_id"])
    
    return render_template('admin/menu.html', menus=menus)

@admin_bp.route('/orders', methods=["GET", "POST"])
def order() :

    db = current_app.config['DB']
    orders = list(db.orders.find({}))
    total_menu = sum(len(order['items']) for order in orders)
    converted_orders = convert_ids_to_strings(orders)
    
    return render_template('admin/orders.html', orders=converted_orders, total_menu=total_menu)

@admin_bp.route('/users', methods=["GET", "POST"])
def user():
    db = current_app.config['DB']
    users = list(db.users.find({}))

    for user in users:
        user['_id'] = str(user['_id'])

    for user in users:
        user['shipping_address'] = user.get('shipping_address', 'No address available')

    return render_template('admin/users.html', users=users)

@admin_bp.route("/sales-chart-data")
def sales_chart_data():
    db = current_app.config['DB']
    
    menus = list(db.menu.find({}))
    menu_sales = {menu['name']: 0 for menu in menus}

    orders = list(db.orders.find({"status": "selesai"}))
    for order in orders:
        for item in order.get('items', []):
            menu_name = item.get('menu_name')
            quantity = int(item.get('quantity', 0))
            if menu_name in menu_sales:
                menu_sales[menu_name] += quantity 

    return {"labels": list(menu_sales.keys()), "data": list(menu_sales.values())}

@admin_bp.route("/bar-chart-data")
def bar_chart_data():
    db = current_app.config['DB']

    menus = list(db.menu.find({}))
    categories = {menu['category']: 0 for menu in menus}

    orders = list(db.orders.find({"status": "selesai"}))
    for order in orders:
        for item in order.get('items', []):
            menu_name = item.get('menu_name')
            quantity = int(item.get('quantity', 0))

            for menu in menus:
                if menu['name'] == menu_name:
                    category = menu.get('category', 'Other')
                    categories[category] += quantity
                    break

    return {
        "labels": list(categories.keys()), 
        "data": list(categories.values())
    }
