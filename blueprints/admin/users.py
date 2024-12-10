from flask import Blueprint, render_template, current_app, request, session, redirect, url_for, jsonify
from bson import ObjectId

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

    for user in users:
        user['shipping_address'] = user.get('shipping_address', 'No address available')

    return render_template('admin/users/index.html', users=users)