from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app, jsonify
from datetime import datetime
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

# Route untuk halaman checkout
@order_bp.route("/", methods=["GET", "POST"])
def checkout():
    db = current_app.config['DB']
    username = session.get('username')

    if not username:
        return redirect(url_for('auth.login'))

    # Ambil data pengguna
    user_data = db.users.find_one({"username": username})

    if not user_data:
        flash("User tidak ditemukan, silakan login kembali.", "danger")
        return redirect(url_for('auth.login'))

    # Ambil data shipping address dari database
    shipping_address = user_data.get("shipping_address", {
        "name": "",
        "address": "",
        "place_type": "",
        "phone": "",
        "email": ""
    })

    return render_template("checkout.html", shipping_address=shipping_address)

# Route untuk memperbarui alamat pengiriman
@order_bp.route("/edit_address", methods=["POST"])
def edit_address():
    db = current_app.config['DB']
    username = session.get('username')

    if not username:
        return redirect(url_for('auth.login'))

    # Ambil data dari form
    name = request.form.get('name', '').strip()
    address = request.form.get('address', '').strip()
    place_type = request.form.get('place_type', '').strip()
    phone = request.form.get('phone', '').strip()
    email = request.form.get('email', '').strip()

    # Validasi input
    if not all([name, address, phone, email]):
        flash("Semua field wajib diisi!", "danger")
        return redirect(url_for('order.checkout'))

    # Update shipping address di database
    new_shipping_address = {
        "name": name,
        "address": address,
        "place_type": place_type,
        "phone": phone,
        "email": email
    }

    db.users.update_one(
        {"username": username},
        {"$set": {"shipping_address": new_shipping_address}}
    )

    flash("Alamat pengiriman berhasil diperbarui!", "success")
    return redirect(url_for('order.checkout'))

# Route untuk menyimpan pesanan
@order_bp.route("/checkout", methods=["POST"])
def store():
    db = current_app.config['DB']
    username = session.get('username')
    data = request.json
    payment_method = data.get('paymentMethod')
    cart_items = list(db.carts.find({"user": username}))
    now = datetime.now()
    time = now.strftime("%B %d, %Y")

    if not username:
        return jsonify({"status": "danger", "message": "User tidak ditemukan, silakan login", "info": "!login"}), 401

    if not payment_method:
        return jsonify({"status": "danger", "message": "Metode pembayaran tidak dipilih", "info": "!paymentMethod"}), 400

    if not cart_items:
        return jsonify({"status": "danger", "message": "Keranjang kosong", "info": "!cart"}), 400

    total_price = sum(item['price'] * item['quantity'] for item in cart_items)

    order = {
        "user": username,
        "items": cart_items,
        "total_price": total_price,
        "payment_method": payment_method,
        "status": "pending",
        "date": time
    }

    order_id = db.orders.insert_one(order).inserted_id

    # Hapus keranjang setelah checkout
    db.carts.delete_many({"user": username})

    return jsonify({"status": "success", "message": "Order berhasil dibuat", "order_id": str(order_id)}), 201

# Route untuk menampilkan halaman terima kasih
@order_bp.route("/thankyou")
def thank_you():
    return render_template("thank-you.html")

# Route untuk menampilkan semua pesanan
@order_bp.route('/all')
def all_orders():
    db = current_app.config['DB']
    orders = list(db.orders.find({}))
    for order in orders:
        order['_id'] = str(order['_id'])

    data = {
        "status": "success",
        "message": "Berhasil mendapatkan semua pesanan",
        "data": orders
    }

    return jsonify(data), 200

# Route untuk menampilkan pesanan berdasarkan username
@order_bp.route('/all/<username>')
def user_orders(username):
    db = current_app.config['DB']
    session_username = session.get('username')

    if not session_username:
        return jsonify({"status": "danger", "message": "User tidak ditemukan, silakan login", "info": "!login"})

    orders = list(db.orders.find({"user": session_username}))

    if not orders:
        return jsonify({"status": "success", "message": "Belum ada pesanan", "info": "!order"})

    converted_orders = convert_ids_to_strings(orders)

    data = {
        "status": "success",
        "message": f"Pesanan milik {username} berhasil diambil",
        "data": converted_orders
    }
    return jsonify(data), 200
