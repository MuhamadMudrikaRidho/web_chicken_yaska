from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app, jsonify
from datetime import datetime
import bcrypt
from pymongo import MongoClient
from bson import ObjectId

order_bp = Blueprint("order", __name__, url_prefix="/order")

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

@order_bp.route("/")
def home():
    # cek di database cart
    return render_template("checkout.html")

@order_bp.route('/all')
def index() :
    db = current_app.config['DB']
    orders = list(db.orders.find({}))
    for order in orders :
        order['_id'] = str(order['_id'])

    data = {
        "status" : "success",
        "message" : "get all orders",
        "data" : orders
    }

    return jsonify(data), 200

@order_bp.route('/all/<username>')
def show(username):
    db = current_app.config['DB']
    user = session.get('username')

    if not user:
        return jsonify({"status": "danger", "message": "User tidak ditemukan, silahkan login", "info": "!login"})

    orders = list(db.orders.find({"user": user}))

    if not orders:
        return jsonify({"status": "success", "message": "User belum melakukan order", "info": "!order"})

    # for order in orders:
    #     order['_id'] = str(order['_id'])

    convertedOrders = convert_ids_to_strings(orders)

    data = {
        "status": "success",
        "message": f"get {username} orders...",
        "data": convertedOrders
    }
    return jsonify(data), 200

@order_bp.route('/checkout', methods=["POST"])
def store() :
    db = current_app.config['DB']
    user = session.get('username')
    data = request.json
    payment_method = data.get('paymentMethod')
    cart_items = list(db.carts.find({"user": user}))
    now = datetime.now()
    time = now.strftime("%B %d, %Y")

    if not user:
        return jsonify({"status" : "danger", "message": "User tidak ditemukan, silakan login", "info" : "!login"}), 401


    if not payment_method:
        return jsonify({"status" : "danger", "message": "Metode pembayaran tidak dipilih", "info" : "!paymentMethod"}), 400


    if not cart_items:
        return jsonify({"status" : "danger", "message": "Cart is empty", "info": "!cart"}), 400

    total_price = sum(item['price'] * item['quantity'] for item in cart_items)

    order = {
        "user": user,
        "items": cart_items,
        "total_price": total_price,
        "payment_method": payment_method, 
        "status": "pending",
        "date" : time
    }

    order_id = db.orders.insert_one(order).inserted_id

    db.carts.delete_many({"user": user})

    return jsonify({"status" : "success", "message": "Order berhasil dibuat", "order_id": str(order_id)}), 201

@order_bp.route("/thankyou")
def greating():
    return render_template("thank-you.html")
