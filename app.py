import os
from os.path import join, dirname
from dotenv import load_dotenv  # type: ignore

from flask import (  # type: ignore
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    jsonify
)

from pymongo import MongoClient  # type: ignore
from bson import ObjectId  # type: ignore

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', login=False)


@app.route("/menu")
def menu():
    # Data produk yang akan dikirim ke template
    products = [
        {"image": "assets/images/hand-picked/favyasaka.jpg",
            "name": "Ayam Bakar Crispy", "price": "Rp.15.000"},
        {"image": "assets/images/hand-picked/chicken.jpg",
            "name": "Chicken + Nasi", "price": "Rp.20.000"},
        {"image": "assets/images/hand-picked/mentai.jpg",
            "name": "Ayam Bakar Mentai + Nasi", "price": "Rp.15.000"},
        {"image": "assets/images/hand-picked/geprek.jpg",
            "name": "Ayam Geprek + Nasi", "price": "Rp.17.000"},
    ]

    # Kirim data produk ke template
    return render_template('menu.html', login=False, products=products)


@app.route('/about')
def about():
    return render_template('about.html', login=False)


port = 5000
debug = True

if __name__ == "__main__":
    app.run('0.0.0.0', port=port, debug=debug)
