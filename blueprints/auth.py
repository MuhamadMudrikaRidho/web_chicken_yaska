from flask import Blueprint, render_template, redirect, url_for, session, request, current_app, jsonify
import re
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

        if len(name) < 2 or not re.match(r"^[a-zA-Z\s]+$", name):
            return "Name must be at least 2 characters and only contain letters and spaces.", 400

        if len(username) < 3 or not re.match(r"^[a-zA-Z0-9_]+$", username):
            return "Username must be at least 3 characters and can only contain letters, numbers, and underscores.", 400

        email = email.lower()
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            return "Invalid email format.", 400

        password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
        if not re.match(password_regex, password):
            return (
                "Password must be at least 8 characters long and contain at least one uppercase letter, "
                "one lowercase letter, and one number.",
                400
            )

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

@auth_bp.route('/check-login')
def isLogin():
    
    if is_logged_in() :
        return jsonify({"isLoggedIn" : True})
    
    return jsonify({"isLoggedIn" : False})
