from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app
from datetime import datetime
import bcrypt

user_bp = Blueprint("user", __name__, url_prefix="/account")

@user_bp.route('/', methods=["GET", "POST"])
def home():
    db = current_app.config['DB']
    
    username = session.get('username')
    if not username:
        return redirect(url_for('auth.login'))

    user_data = db.users.find_one({"username": username})
    now = datetime.now().strftime('%Y-%m-%d')
    orders = list(db.orders.find({"user": username}))
    wishlists = list(db.wishlists.find({"user": username}))

    total_orders = len(orders)
    total_wishlist = len(wishlists)

    if request.method == "POST":
        name = request.form.get('name')
        username_rec = request.form.get('username')
        email = request.form.get('email')
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')

        if bcrypt.checkpw(old_password.encode('utf-8'), user_data['password'].encode('utf-8')):
            hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            db.users.update_one(
                {"username": username},
                {"$set": {
                    "password": hashed_new_password.decode('utf-8'),
                    "name" : name,
                    "username" : username_rec,
                    "email" : email,
                    }}
            )
            flash("Account updated successfully!", "success")
        else:
            flash("Old password is incorrect.", "danger")
        return redirect(url_for('user.home'))

    shipping_address = user_data.get("shipping_address")
    return render_template('account.html', user_data=user_data, now=now, shipping_address=shipping_address, total_orders=total_orders, total_wishlist=total_wishlist)

@user_bp.route('/edit_address', methods=["POST"])
def edit_address():
    db = current_app.config['DB']
    
    username = session.get('username')
    if not username:
        return redirect(url_for('auth.login'))

    name = request.form.get('name', '').strip()
    address = request.form.get('address', '').strip()
    phone = request.form.get('phone', '').strip()
    place_type = request.form.get('place_type', '').strip()

    if not all([name, address, phone]):
        flash("Semua field wajib diisi!", "danger")
        return redirect(url_for('user.home'))

    shipping_address = {
        "name": name,
        "address": address,
        "phone": phone,
        "place_type": place_type,
    }

    db.users.update_one(
        {"username": username},
        {"$set": {"shipping_address": shipping_address}}
    )

    flash("Alamat berhasil diperbarui!", "success")
    return redirect(url_for('user.home'))
