from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app, send_from_directory
from datetime import datetime
import bcrypt
import re
import os
from werkzeug.utils import secure_filename

user_bp = Blueprint("user", __name__, url_prefix="/account")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@user_bp.route('/uploads/<path:filename>')
def uploaded_file(filename):
    upload_folder = current_app.config['UPLOAD_FOLDER']
    return send_from_directory(upload_folder, filename)

@user_bp.route('/', methods=["GET", "POST"])
def home():
    db = current_app.config['DB']

    username = session.get('username')
    if not username:
        return redirect(url_for('auth.login'))

    user_data = db.users.find_one({"username": username})
    now = datetime.now().strftime("%B %d, %Y")
    orders = list(db.orders.find({"user": username}))
    wishlists = list(db.wishlists.find({"user": username}))

    total_orders = len(orders)
    total_wishlist = len(wishlists)

    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')

        if new_password:
            password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
            if not re.match(password_regex, new_password):
                return (
                    "Password must be at least 8 characters long and contain at least one uppercase letter, "
                    "one lowercase letter, and one number.",
                    400
                )

        if bcrypt.checkpw(old_password.encode('utf-8'), user_data['password'].encode('utf-8')):
            if new_password : 
                hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                new_password = hashed_new_password.decode('utf-8')
            else :
                new_password = user_data['password']
            db.users.update_one(
                {"username": username},
                {"$set": {
                    "password": new_password,
                    "name": name,
                    "email": email,
                }}
            )
            flash("Account updated successfully!", "success")
        else:
            flash("Old password is incorrect.", "danger")
        return redirect(url_for('user.home'))

    shipping_address = user_data.get('shipping_address') or {}

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

@user_bp.route('/upload_profile_pic', methods=["POST"])
def upload_profile_pic():
    db = current_app.config['DB']
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    profile_folder = os.path.join(upload_folder, 'profiles')

    if not os.path.exists(profile_folder):
        os.makedirs(profile_folder)

    username = session.get('username')
    if not username:
        flash("Anda harus login untuk mengubah foto profil.", "danger")
        return redirect(url_for('auth.login'))

    image = request.files.get('profile_pic')
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        today = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        file_fullname = f"profile-{username}-{today}.{filename.rsplit('.', 1)[1].lower()}"
        file_path = os.path.join(profile_folder, file_fullname)
        image.save(file_path)

        # Update path foto profil di database
        image_url = f'uploads/profiles/{file_fullname}'
        db.users.update_one(
            {"username": username},
            {"$set": {"profile_pic": image_url}}
        )
        flash("Foto profil berhasil diperbarui!", "success")
    else:
        print(image)
        flash("File yang diunggah tidak valid. Pastikan format file PNG, JPG, atau JPEG.", "danger")

    return redirect(url_for('user.home'))
