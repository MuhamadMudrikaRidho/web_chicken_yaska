from flask import Blueprint, render_template, redirect, url_for, session, request, current_app
import bcrypt

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

def is_logged_in():
    return 'username' in session

@auth_bp.route('/login', methods=["POST", "GET"])
def login():
    
    if is_logged_in():
      return redirect('/')
    
    db = current_app.config['DB']
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            return render_template('login.html', message={'info': "Provide both email and password", 'type': "danger"})

        login_user = db.users.find_one({'email': email})
        if login_user and bcrypt.checkpw(password.encode('utf-8'), login_user['password'].encode('utf-8')):
            session['username'] = login_user['username']
            return redirect(url_for('menu.home')) 
        return render_template('login.html', message={'info': "Invalid Email or Password", 'type': "danger"})
    return render_template('login.html')

@auth_bp.route('/register', methods=["POST", "GET"])
def register():

    if is_logged_in():
            return redirect(url_for('menu.home'))
  
    db = current_app.config['DB']
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')

        if not email or not password or not name or not username:
            return "All fields are required!", 400

        email = email.lower()
        username = username.lower()
        existing_user = db.users.find_one({"email": email})
        existing_username = db.users.find_one({"username": username})

        if existing_username:
            return "That username already exists", 400
        if existing_user:
            return "That email already exists", 400

        if not existing_user and not existing_username:
            hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            doc = {"name": name, "username": username, "email": email, "password": hashpass.decode('utf-8')}
            db.users.insert_one(doc)
            return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
