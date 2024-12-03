from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app
from datetime import datetime
import bcrypt
from pymongo import MongoClient

order_bp = Blueprint("order", __name__, url_prefix="/order")

@order_bp.route("/")
def home():
    return render_template("checkout.html")

@order_bp.route("/thankyou")
def greating():
    return render_template("thank-you.html")