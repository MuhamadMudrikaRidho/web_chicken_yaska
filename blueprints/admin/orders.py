from flask import Blueprint, render_template, current_app, request, session, redirect, url_for, flash
from bson import ObjectId
from datetime import datetime

admin_orders_bp = Blueprint("admin_orders", __name__, url_prefix="/admin/orders")

@admin_orders_bp.before_request
def restrict_to_admins():
    
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    if not session.get('isAdmin', False):
        return redirect('/')

@admin_orders_bp.context_processor
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
    
@admin_orders_bp.route("/")
def index() :
    db = current_app.config['DB']
    orders = list(db.orders.find({}))
    total_menu = sum(len(order['items']) for order in orders)
    converted_orders = convert_ids_to_strings(orders)
    
    return render_template('admin/orders/index.html', orders=converted_orders, total_menu=total_menu)

@admin_orders_bp.route('/create')
def create() :

    db = current_app.config['DB']
    menus = list(db.menu.find({}))
    for menu in menus :
        menu['_id'] = str(menu['_id'])
    return render_template('admin/orders/create.html', menus=menus)

@admin_orders_bp.route('/', methods=["POST"])
def store() :

    db = current_app.config['DB']
    
    try:
        user = session.get('username', 'Anonymous')
        selected_menus = request.form.getlist('menu_id[]')

        if not selected_menus:
            flash("Anda harus memilih setidaknya satu menu.", "danger")
            return redirect('/admin/orders/create')
        
        items = []
        total_price = 0

        for menu_id in selected_menus:
            quantity = int(request.form.get(f'quantity_{menu_id}', 1))
            menu = db.menu.find_one({'_id': ObjectId(menu_id)})

            if menu:
                item = {
                    "menu_id": str(menu['_id']),
                    "menu_name": menu['name'],
                    "price": menu['price'],
                    "quantity": quantity
                }
                items.append(item)
                total_price += menu['price'] * quantity

        delivery_charge = 0
        payment_method = "Bayar dan Ambil Di Outlet"
        address = {
            "name": request.form.get('address_name', ''),
            "address": request.form.get('address_detail', ''),
            "placeType": request.form.get('address_type', ''),
            "phone": request.form.get('address_phone', ''),
            "email": request.form.get('address_email', ''),
            "notes": request.form.get('address_notes', '')
        }
        status = "diproses"
        date = datetime.now().strftime("%B %d, %Y")

        # Data pesanan
        order = {
            "user": user,
            "items": items,
            "delivery_charge": delivery_charge,
            "total_price": total_price,
            "payment_method": payment_method,
            "address": address,
            "status": status,
            "date": date
        }

        db.orders.insert_one(order)

        flash("Pesanan baru berhasil ditambahkan!", "success")
        return redirect('/admin/orders')
    except Exception as e:
        flash(f"Terjadi kesalahan: {e}", "danger")
        return redirect('/admin/orders')

@admin_orders_bp.route('/<order_id>')
def show(order_id) :
    db = current_app.config['DB']
    order = db.orders.find_one({'_id' : ObjectId(order_id)})
    converted_order = convert_ids_to_strings(order)

    menu_items = converted_order['items']

    return render_template('admin/orders/detail.html', order=converted_order, menus=menu_items)

@admin_orders_bp.route('/<order_id>/update-status', methods=["POST"])
def update(order_id) :
    db = current_app.config['DB']
    status = request.form.get('status')
    db.orders.update_one({'_id' : ObjectId(order_id)}, {"$set" : {"status" : status}})

    flash(f'status dengan id {order_id} berhasil diupdate menjadi {status}', "success")
    return redirect('/admin/orders')

@admin_orders_bp.route('/<order_id>/print')
def print(order_id) :
    db = current_app.config['DB']
    order = db.orders.find_one({'_id' : ObjectId(order_id)})
    converted_order = convert_ids_to_strings(order)

    menu_items = converted_order['items']

    return render_template('admin/orders/print.html', order=converted_order, menus=menu_items)