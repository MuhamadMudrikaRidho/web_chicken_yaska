from flask import Blueprint, render_template, session, redirect, url_for, current_app

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

@cart_bp.route("/")
def home():
    if 'username' not in session:
        return redirect(url_for('auth.login'))

    carts = [
        {"image": "assets/images/hand-picked/favyasaka.jpg",
         "name": "Ayam Bakar Crispy", "price": 15000, "category": "Ayam"},
        {"image": "assets/images/hand-picked/chicken.jpg",
         "name": "Chicken + Nasi", "price": 20000, "category": "Ayam"},
        {"image": "assets/images/hand-picked/mentai.jpg",
         "name": "Ayam Bakar Mentai + Nasi", "price": 15000, "category": "Ayam"},
        {"image": "assets/images/hand-picked/geprek.jpg",
         "name": "Ayam Geprek + Nasi", "price": 17000, "category": "Ayam"},
    ]

    return render_template('cart.html', carts=carts)
