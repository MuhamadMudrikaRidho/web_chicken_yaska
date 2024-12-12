from flask import Blueprint, render_template, session, redirect, url_for, current_app, request, jsonify
from bson import ObjectId

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

@cart_bp.route("/")
def home():
    if 'username' not in session:
        return redirect(url_for('auth.login'))

    return render_template('cart.html')

@cart_bp.route('/all')
def index():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    user = session['username']
    db = current_app.config['DB']

    cart_items = db.carts.find({'user': user})
    items = []
    total = 0
    for item in cart_items:
        menu = db.menu.find_one({'_id': ObjectId(item['menu_id'])})
        items.append({
            'id' : str(item['_id']),
            'menu_name': menu['name'],
            'menu_category' : menu['category'],
            'menu_image' : menu['image'],
            'quantity': item['quantity'],
            'price': menu['price'],
        })
        total += (menu['price'] * item['quantity'])
    
    data = {
        "stats" : "success",
        "message" : "Dapatkan data keranjang Anda",
        "data" : items,
        "total" : total
    }

    return jsonify(data)

@cart_bp.route('/<menu_id>', methods=["POST"])
def store(menu_id) :
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    user = session['username']
    db = current_app.config['DB']
    quantity = request.form.get('quantity')
    menu = db.menu.find_one({'_id' : ObjectId(menu_id)})
    if not menu : 
        return jsonify({"status" : "error", "message" : "menu tidak ditemukan"}), 404
    cart = db.carts.find_one({'menu_id': menu['_id'], "user" : user})
    if cart:
        db.carts.update_one(
            {'_id': cart['_id']},
            {'$set': {'quantity': cart['quantity'] + int(quantity)}}
        )
    else:
        db.carts.insert_one({
            'menu_id': ObjectId(menu_id),
            'menu_name' : menu['name'],
            'price' : menu['price'],
            'quantity': int(quantity),
            'user' : user
        })

    data = {
        "status" : "success",
        "message" : "Menu Berhasil ditambahkan ke keranjang!"
    }

    return jsonify(data)

@cart_bp.route('/update', methods=["POST"])
def update_cart():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    try:
        data = request.json
        cart_id = ObjectId(data.get('cart_id'))
        quantity = data.get('quantity')
        db = current_app.config['DB']

        if not cart_id or quantity is None or quantity < 1:
            return jsonify({"error": "Invalid data"}), 400

        cart_item = db.carts.find_one({"_id": cart_id})
        if not cart_item:
            return jsonify({"error": "Cart item not found"}), 404

        db.carts.update_one(
            {"_id": cart_id},
            {"$set": {"quantity": quantity}}
        )

        return jsonify({"message": "kuantitas diperbarui"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@cart_bp.route('/<cart_id>/destroy', methods=["post"])
def destroy(cart_id) :
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    user = session['username']
    db = current_app.config['DB']
    db.carts.delete_one({'_id': ObjectId(cart_id), "user" : user})

    data = {
        "status" : "success",
        "message" : "Menu dihapus dari Keranjang"
    }
    return jsonify(data)