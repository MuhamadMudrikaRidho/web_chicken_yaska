from flask import Blueprint, render_template, current_app, request, session, redirect, url_for, flash, jsonify
from bson import ObjectId
import bcrypt

admin_users_bp = Blueprint("admin_users", __name__, url_prefix="/admin/users")

@admin_users_bp.before_request
def restrict_to_admins():
    
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    if not session.get('isAdmin', False):
        return redirect('/')

@admin_users_bp.context_processor
def inject_admin_data():
    db = current_app.config['DB']
    user = session.get('username')
    admin = db.users.find_one({"username": user}) if user else None
    return {'admin': admin}

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
    
@admin_users_bp.route("/")
def index() :
    db = current_app.config['DB']
    users = list(db.users.find({}))

    for user in users:
        user['_id'] = str(user['_id'])
        user['total_orders'] = db.orders.count_documents({"user": user['username'], "status" : "selesai"})
        user['shipping_address'] = user.get('shipping_address', 'No address available')

    return render_template('admin/users/index.html', users=users)

@admin_users_bp.route('/', methods=["POST"])
def store() :
    db = current_app.config['DB']
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = bcrypt.hashpw(request.form.get('password').encode('utf-8'), bcrypt.gensalt())
    isAdmin = False  
    if request.form.get('isAdmin') == "admin" :
        isAdmin = True
          

    doc = {
        "name" : name,
        "username" : username,
        "email" : email,
        "password" : password.decode('utf-8'),
        "isAdmin" : isAdmin,
    }

    db.users.insert_one(doc)

    flash("pengguna baru berhasil ditambahkan", "success")

    return redirect('/admin/users')

@admin_users_bp.route('/create')
def create() :

    return render_template('admin/users/create.html')

@admin_users_bp.route('/<user_id>/edit')
def edit(user_id) :

    db = current_app.config['DB']
    user = db.users.find_one({"_id" : ObjectId(user_id)})

    return render_template('admin/users/edit.html', user=user)

@admin_users_bp.route('/<user_id>/edit', methods=["POST"])
def update(user_id) :
    db = current_app.config['DB']

    old_user_data = db.users.find_one({"_id" : ObjectId(user_id)})

    name = request.form.get('name', old_user_data['name'])
    email = request.form.get('email', old_user_data['email'])
    if request.form.get('password') : 
        reqPassword = bcrypt.hashpw(request.form.get('password').encode('utf-8'), bcrypt.gensalt())
        password = reqPassword.decode('utf-8')
    else : 
        password = old_user_data['password']
    isAdmin = False
    if request.form.get('isAdmin') == "admin" :
        isAdmin = True
          

    doc = {
        "name" : name,
        "email" : email,
        "password" : password,
        "isAdmin" : isAdmin,
    }

    db.users.update_one({"_id" : ObjectId(user_id)}, {"$set" : doc})
    flash(f"user dengan id {user_id} berhasil diubah", "success")
    return redirect('/admin/users')

@admin_users_bp.route('/<user_id>/destroy', methods=["POST"])
def destroy(user_id) :
    db = current_app.config["DB"]
    user = db.users.find_one({"_id" : ObjectId(user_id)})
    if not user :
        return jsonify({"status" : "error", "message" : "user tidak ditemukan"}), 404
    db.users.delete_one({"_id" : ObjectId(user_id)})
    db.wishlists.delete_many({"user" : user['username']})
    db.carts.delete_many({"user" : user['username']})

    flash(f"user dengan id {user_id} berhasil dihapus", "success")
    return redirect('/admin/users')