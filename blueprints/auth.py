from flask import Blueprint, render_template, redirect, url_for, session, request, current_app, jsonify, flash
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
        return render_template('login.html', message={'info': "Email atau Kata Sandi Tidak Valid", 'type': "danger"})
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
            return "Semua kolom wajib diisi!", 400

        if len(name) < 2 or not re.match(r"^[a-zA-Z\s]+$", name):
            return "Nama harus minimal 2 karakter dan hanya mengandung huruf dan spasi.", 400

        if len(username) < 3 or not re.match(r"^[a-zA-Z0-9_]+$", username):
            return "Nama pengguna harus minimal 3 karakter dan hanya boleh berisi huruf, angka, dan garis bawah.", 400

        email = email.lower()
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            return "Format email tidak valid.", 400

        password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
        if not re.match(password_regex, password):
            return (
                "Kata sandi harus minimal 8 karakter dan mengandung setidaknya satu huruf kapital, "
                "satu huruf kecil, dan satu angka.",
                400
            )

        username = username.lower()
        existing_user = db.users.find_one({"email": email})
        existing_username = db.users.find_one({"username": username})

        if existing_username:
            flash('That username already exists', 'danger')
            return redirect(url_for('auth.register'))
        if existing_user:
            flash('That email already exists', 'danger')
            return redirect(url_for('auth.register'))

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
