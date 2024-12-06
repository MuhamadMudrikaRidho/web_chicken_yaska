
from flask import Blueprint, render_template, current_app, request, session
from bson import ObjectId

menu_bp = Blueprint("menu", __name__, url_prefix="/menu")

@menu_bp.route("/")
def home():
    db = current_app.config['DB']
    sort_option = request.args.get('sort', 'default') 

    if sort_option == 'price_asc':
        menus = list(db.menu.find({}).sort('price', 1))
    elif sort_option == 'price_desc':
        menus = list(db.menu.find({}).sort('price', -1)) 
    else:
        menus = list(db.menu.find({})) 

    user = "hehe"
    if 'username' in session : 
        user = session['username']
    isWishlisted = False

    for menu in menus:
        menu['_id'] = str(menu['_id'])
        if db.wishlists.find_one({'menu_id' : menu['_id'], 'user' : user}) : 
            isWishlisted = True

    return render_template("menu.html", menus=menus, current_sort=sort_option, isWishlisted=isWishlisted)

@menu_bp.route("/<id>")
def detail(id):
    db = current_app.config['DB']
    menu = db.menu.find_one({"_id": ObjectId(id)})
    user = "hehe"
    if 'username' in session : 
        user = session['username']
    
    isWishlisted = False

    if db.wishlists.find_one({'menu_id' : menu['_id'], 'user' : user}) : 
            isWishlisted = True

    if not menu:
        return "Menu not found", 404

    menu['_id'] = str(menu['_id'])
    menu['price'] = menu['price']
    count_price = menu['price'] + 3000
    
    return render_template('detail-menu.html', menu=menu, count_price=count_price, isWishlisted=isWishlisted)
