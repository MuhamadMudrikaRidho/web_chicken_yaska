import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime



from functools import wraps

from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    jsonify,
    session,
    flash
)

import bcrypt

from pymongo import MongoClient
from bson import ObjectId

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)
app.secret_key = "chicken_yasaka"

def is_logged_in():
    return 'username' in session

def redirect_if_logged_in(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if is_logged_in():
            return redirect(url_for('home'))
        return func(*args, **kwargs)
    return decorated_function

def redirect_if_not_logged_in(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return decorated_function


@app.route("/")
def home():
    return render_template('index.html', login=False)

@app.route("/menu")
def menu():
    products = list(db.menu.find({}))

    for product in products:
        product['_id'] = str(product['_id'])

    return render_template('menu.html', products=products)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=["POST", "GET"])
@redirect_if_logged_in
def login():
    
    if request.method == "POST" : 
      email = request.form.get('email')
      password = request.form.get('password')

      if not email or not password:
          return render_template('login.html', message={'info': "Please provide both email and password", 'type': "danger"})

      login_user = db.users.find_one({'email': email})

      if login_user: 
          if bcrypt.checkpw(password.encode('utf-8'), login_user['password'].encode('utf-8')):
              session['username'] = login_user['username']
              return redirect(url_for('home'))

      return render_template('login.html', message={'info': "Invalid Email or Password", 'type': "danger"})

    return render_template('login.html')


@app.route('/register', methods=["POST", "GET"])
@redirect_if_logged_in
def register():
    if request.method == "POST" :  
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

      if existing_username :
          return "That username already exists", 400
      
      if existing_user : 
          return "That email already exists", 400

      if existing_user is None and existing_username is None:
          hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
          doc = {
              "name": name,
              "username" : username,
              "email": email,
              "password": hashpass.decode('utf-8')
          }
          db.users.insert_one(doc)
          return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@redirect_if_not_logged_in
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/cart')
@redirect_if_not_logged_in
def cart() :
    carts = [
        {"image": "assets/images/hand-picked/favyasaka.jpg",
            "name": "Ayam Bakar Crispy", "price": "Rp.15.000", "category" : "Ayam"},
        {"image": "assets/images/hand-picked/chicken.jpg",
            "name": "Chicken + Nasi", "price": "Rp.20.000", "category" : "Ayam"},
        {"image": "assets/images/hand-picked/mentai.jpg",
            "name": "Ayam Bakar Mentai + Nasi", "price": "Rp.15.000", "category" : "Ayam"},
        {"image": "assets/images/hand-picked/geprek.jpg",
            "name": "Ayam Geprek + Nasi", "price": "Rp.17.000", "category" : "Ayam"},
    ]
    return render_template('cart.html', carts=carts)

@app.route('/account', methods=["GET", "POST"])
@redirect_if_not_logged_in
def account():
    username = session.get('username')  # Langsung ambil username dari session
    now = datetime.now().strftime('%Y-%m-%d')

    # Ambil data pengguna dari koleksi 'users' berdasarkan username
    user_data = db.users.find_one({"username": username})

    # Jika method POST (untuk mengubah data, misalnya password)
    if request.method == "POST":
        # Untuk mengubah password
        if 'old_password' in request.form and 'new_password' in request.form:
            old_password = request.form.get('old_password')
            new_password = request.form.get('new_password')

            # Verifikasi apakah password lama sesuai dengan yang ada di database
            if bcrypt.checkpw(old_password.encode('utf-8'), user_data['password'].encode('utf-8')):
                # Jika password lama benar, lakukan pembaruan password
                hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                db.users.update_one(
                    {"username": username},
                    {"$set": {"password": hashed_new_password.decode('utf-8')}}
                )
                flash("Password updated successfully!", "success")
            else:
                flash("Old password is incorrect.", "danger")

        return redirect(url_for('account'))

    return render_template('account.html', 
                           user_data=user_data,  # Kirim data pengguna
                           now=now)



@app.route('/wishlist')
@redirect_if_not_logged_in
def wishlist():
    return render_template('wishlist.html')

port = 5000
debug = True

if __name__ == "__main__":
    app.run('0.0.0.0', port=port, debug=debug)
