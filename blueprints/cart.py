from flask import Blueprint, render_template, session, redirect, url_for, current_app, request, flash, jsonify
from bson import ObjectId

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

@cart_bp.route("/")
def home():
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
    
    return render_template('cart.html', carts=items, total=total)

@cart_bp.route('/<menu_id>', methods=["POST"])
def store(menu_id) :
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    user = session['username']
    db = current_app.config['DB']
    quantity = request.form.get('quantity', 1)
    
    cart = db.carts.find_one({'menu_id': ObjectId(menu_id), "user" : user})
    if cart:
        db.carts.update_one(
            {'_id': cart['_id']},
            {'$set': {'quantity': cart['quantity'] + int(quantity)}}
        )
    else:
        db.carts.insert_one({
            'menu_id': ObjectId(menu_id),
            'quantity': int(quantity),
            'user' : user
        })

    return jsonify({"message": "Menu Successfully added to cart!"})

@cart_bp.route('/update_quantity', methods=["POST"])
def update_quantity():
    try:

        data = request.json
        print("Received data:", data)
        db = current_app.config['DB']
        cart_id = request.json.get('cart_id')
        new_quantity = request.json.get('quantity') 

        if not cart_id or not new_quantity or int(new_quantity) < 1:
            return jsonify({"error": "Invalid data"}), 400

        db.carts.update_one(
            {'_id': ObjectId(cart_id)},
            {'$set': {'quantity': int(new_quantity)}}
        )

        return jsonify({"success": True, "message": "Quantity updated"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@cart_bp.route('/<cart_id>/destroy', methods=["post"])
def destroy(cart_id) :
    user = session['username']
    db = current_app.config['DB']
    db.carts.delete_one({'_id': ObjectId(cart_id), "user" : user})

    flash("Menu deleted from cart", "success")
    return redirect(url_for('cart.home'))