from templates import format_rupiah
from config import DevelopmentConfig
from bson import ObjectId

from blueprints.auth import auth_bp
from blueprints.menu import menu_bp
from blueprints.user import user_bp
from blueprints.cart import cart_bp
from blueprints.wishlist import wishlist_bp
from blueprints.order import order_bp


import os

from flask import (
    Flask,
    render_template,
    session,
    current_app
)

from pymongo import MongoClient

app = Flask(__name__)

ENV = os.getenv("FLASK_ENV", "development")

if ENV == "development":
    app.config.from_object(DevelopmentConfig)

client = MongoClient(app.config['MONGODB_URI'])
app.config['DB'] = client[app.config['DB_NAME']]

app.register_blueprint(auth_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(user_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(wishlist_bp)
app.register_blueprint(order_bp)

app.template_filter('format_rupiah')(format_rupiah)

def is_logged_in():
    return 'username' in session

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

port = 5000
debug = True

if __name__ == "__main__":
    app.run('0.0.0.0', port=port, debug=debug)
