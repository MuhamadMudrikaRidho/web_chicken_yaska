from flask import Blueprint, render_template, session, redirect, url_for, current_app

wishlist_bp = Blueprint("wishlist", __name__, url_prefix="/wishlist")

@wishlist_bp.route("/")
def home():
    if 'username' not in session:
        return redirect(url_for('auth.login'))

    products = [
        {"image": "assets/images/hand-picked/favyasaka.jpg",
         "name": "Ayam Bakar Crispy", "price": 15000},
        {"image": "assets/images/hand-picked/chicken.jpg",
         "name": "Chicken + Nasi", "price": 20000},
        {"image": "assets/images/hand-picked/mentai.jpg",
         "name": "Ayam Bakar Mentai + Nasi", "price": 15000},
        {"image": "assets/images/hand-picked/geprek.jpg",
         "name": "Ayam Geprek + Nasi", "price": 17000},
    ]

    return render_template('wishlist.html', products=products)
