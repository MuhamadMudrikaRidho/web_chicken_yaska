from flask import Blueprint, render_template, current_app
from bson import ObjectId

menu_bp = Blueprint("menu", __name__, url_prefix="/menu")

@menu_bp.route("/")
def home():
    db = current_app.config['DB']
    menus = list(db.menu.find({}))

    for menu in menus:
        menu['_id'] = str(menu['_id'])

    return render_template("menu.html", menus=menus)

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
