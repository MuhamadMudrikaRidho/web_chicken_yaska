from flask import Blueprint, render_template, current_app, request, session, redirect, url_for, jsonify, flash
from bson import ObjectId
from datetime import datetime
import os

admin_menu_bp = Blueprint("admin_menu", __name__, url_prefix="/admin/menu")

@admin_menu_bp.before_request
def restrict_to_admins():
    
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    if not session.get('isAdmin', False):
        return redirect('/')

@admin_menu_bp.context_processor
def inject_admin_data():
    db = current_app.config['DB']
    user = session.get('username')
    admin = db.users.find_one({"username": user}) if user else None
    return {'admin': admin}

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    
@admin_menu_bp.route("/", methods=["GET", "POST"])
def index():

    db = current_app.config['DB']
    
    if request.method == "POST":
        upload_folder = current_app.config["UPLOAD_FOLDER"]
        menu_folder = os.path.join(upload_folder, 'menu')

        # Buat direktori jika belum ada
        if not os.path.exists(menu_folder):
            os.makedirs(menu_folder)

        name = request.form.get('name')
        category = request.form.get('category')
        price = int(request.form.get('price'))
        image = request.files.get('image')
        description = request.form.get('description')

        now = datetime.now()
        today = now.strftime("%Y-%m-%d-%H-%M-%S")

        # Validasi file
        if image and allowed_file(image.filename):
            extensionFile = image.filename.split('.')[-1]
            fileFullName = f"menu-{today}.{extensionFile}"
            file_saveto = os.path.join(menu_folder, fileFullName)
            image.save(file_saveto)
        else:
            flash("Format file tidak valid", "danger")
            return render_template('admin/menu/create.html')

        # Validasi lainnya
        if not all([name, category, price, description]):
            flash("Data tidak lengkap", "danger")
            return jsonify({"status": "error", "message": "Incomplete data"}), 400

        doc = {
            "name": name,
            "category": category,
            "price": price,
            "image": f'uploads/menu/{fileFullName}',
            "description": description
        }

        db.menu.insert_one(doc)

        flash("Menu baru berhasil ditambahkan", "success")
        return redirect('/admin/menu')
    
    menus = list(db.menu.find({}))
    
    for menu in menus :
        menu["_id"] = str(menu["_id"])
    
    return render_template('admin/menu/index.html', menus=menus)

@admin_menu_bp.route('/<menu_id>')
def show(menu_id) :

    db = current_app.config['DB']
    menu = db.menu.find_one({'_id' : ObjectId(menu_id)})
  
    return render_template('admin/menu/detail.html', menu=menu)
  
@admin_menu_bp.route('/create')
def create() :
    return render_template('admin/menu/create.html')


@admin_menu_bp.route('/<menu_id>/edit')
def edit(menu_id) :

    db = current_app.config['DB']
    menu = db.menu.find_one({'_id' : ObjectId(menu_id)})
    menu['_id'] = str(menu['_id'])
    return render_template('admin/menu/edit.html', menu=menu)

@admin_menu_bp.route('/<menu_id>/edit', methods=["POST"])
def update(menu_id):
    db = current_app.config['DB']
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    menu_folder = os.path.join(upload_folder, 'menu')

    if not os.path.exists(menu_folder):
        os.makedirs(menu_folder)

    name = request.form.get('name')
    category = request.form.get('category')
    price = int(request.form.get('price'))
    description = request.form.get('description')
    image = request.files.get('image')

    if not all([name, category, price, description]):
        flash("Data tidak lengkap", "danger")
        return redirect(f'/admin/menu/{menu_id}/edit')

    if image and allowed_file(image.filename):
        extensionFile = image.filename.split('.')[-1]
        today = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        fileFullName = f"menu-{today}.{extensionFile}"
        file_saveto = os.path.join(menu_folder, fileFullName)
        image.save(file_saveto)

        image_path = f'uploads/menu/{fileFullName}'
    else:
        menu = db.menu.find_one({"_id": ObjectId(menu_id)})
        image_path = menu.get('image')

    # Update data menu di database
    db.menu.update_one(
        {"_id": ObjectId(menu_id)},
        {"$set": {
            "name": name,
            "category": category,
            "price": price,
            "description": description,
            "image": image_path
        }}
    )

    flash(f"Menu dengan id {menu_id} berhasil diubah", "success")
    return redirect('/admin/menu')

@admin_menu_bp.route('/<menu_id>/destroy', methods=["POST"])
def destroy(menu_id):
    db = current_app.config['DB']
    menu = db.menu.find_one({"_id": ObjectId(menu_id)})

    if menu:
        image_path = menu.get('image')
        if image_path:
            file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], image_path)
            if os.path.exists(file_path):
                os.remove(file_path)

        db.menu.delete_one({"_id": ObjectId(menu_id)})

        flash(f"Menu dengan id {menu_id} berhasil dihapus", "success")
        return redirect('/admin/menu')
    else:
        flash(f"Menu dengan id {menu_id} tidak ditemukan", "danger")
        return jsonify({"status": "error", "message": "Menu not found"}), 404
