<<<<<<< HEAD
from flask import Blueprint, render_template, current_app, session
=======
from flask import Blueprint, render_template, current_app, request
>>>>>>> 982d8ae700fd933afa64c1c718f9d7f2576160a1
from bson import ObjectId

menu_bp = Blueprint("menu", __name__, url_prefix="/menu")

@menu_bp.route("/")
def home():
    db = current_app.config['DB']
    sort_option = request.args.get('sort', 'default')  # Ambil parameter sort, default jika tidak ada

    # Menentukan urutan berdasarkan opsi sort
    if sort_option == 'price_asc':
        menus = list(db.menu.find({}).sort('price', 1))  # Ascending (rendah ke tinggi)
    elif sort_option == 'price_desc':
        menus = list(db.menu.find({}).sort('price', -1))  # Descending (tinggi ke rendah)
    else:
        menus = list(db.menu.find({}))  # Tanpa pengurutan

    user = session['username']
    isWishlisted = False

    for menu in menus:
        menu['_id'] = str(menu['_id'])
        if db.wishlists.find_one({'menu_id' : ObjectId(menu['_id']), 'user' : user}) : 
            isWishlisted = True

<<<<<<< HEAD
    return render_template("menu.html", menus=menus, isWishlisted=isWishlisted)
=======
    return render_template("menu.html", menus=menus, current_sort=sort_option)
>>>>>>> 982d8ae700fd933afa64c1c718f9d7f2576160a1

@menu_bp.route("/<id>")
def detail(id):
    db = current_app.config['DB']
    menu = db.menu.find_one({"_id": ObjectId(id)})

    if not menu:
        return "Menu not found", 404

    menu['_id'] = str(menu['_id'])
    menu['price'] = menu['price']
    count_price = menu['price'] + 3000
    
    return render_template('detail-menu.html', menu=menu, count_price=count_price)
