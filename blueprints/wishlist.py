from flask import Blueprint, render_template, session, redirect, url_for, current_app, jsonify
from bson import ObjectId

wishlist_bp = Blueprint("wishlist", __name__, url_prefix="/wishlist")

@wishlist_bp.route("/")
def home():
    if 'username' not in session:
        return redirect(url_for('auth.login'))

    return render_template('wishlist.html')

@wishlist_bp.route('/all')
def index() :
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    user = session['username']
    db = current_app.config['DB']

    wishlist_items = db.wishlists.find({'user': user})
    items = []
    for item in wishlist_items:
        menu = db.menu.find_one({'_id': ObjectId(item['menu_id'])})
        items.append({
            'id' : str(item['_id']),
            'menu_id' : str(menu['_id']),
            'menu_name': menu['name'],
            'menu_image' : menu['image'],
            'price': menu['price'],
        })

    data = {
        "status" : "success",
        "message" : "get your wishlist data",
        "data" : items
    }
    
    return jsonify(data)

@wishlist_bp.route('/<menu_id>', methods=["POST"])
def store(menu_id) : 
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    user = session['username']
    db = current_app.config['DB']
    
    wishlist = db.wishlists.find_one({'menu_id': ObjectId(menu_id), "user" : user})
    data = {
        "status" : "success",
        "message" : "menu berhasil ditambahkan ke list keinginan Anda"
    }

    if wishlist:
        data = {
            "status" : "danger",
            "message" : "menu ini telah ditambahkan ke list keinginan Anda"
        }
    else:
        db.wishlists.insert_one({
            'menu_id': ObjectId(menu_id),
            'user' : user
        })

    
    return jsonify(data)

@wishlist_bp.route('/<menu_id>/destroy', methods=["post"])
def destroy(menu_id) : 
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    user = session['username']
    db = current_app.config['DB']
    db.wishlists.delete_one({'menu_id': ObjectId(menu_id), "user" : user})
    
    data = {
        "status" : "success",
        "message" : "menu berhasil dihapus dari list keinginan Anda"
    }

    return jsonify(data)