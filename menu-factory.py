from config import DevelopmentConfig
from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

ENV = os.getenv("FLASK_ENV", "development")

if ENV == "development":
    app.config.from_object(DevelopmentConfig)

client = MongoClient(app.config['MONGODB_URI'])
db = client[app.config['DB_NAME']]

print("run migration...")

db.menu.drop()

doc = [
  {"image": "assets/images/hand-picked/favyasaka.jpg",
    "name": "Ayam Bakar Crispy", "price": 15000},
  {"image": "assets/images/hand-picked/chicken.jpg",
    "name": "Chicken + Nasi", "price": 20000},
  {"image": "assets/images/hand-picked/mentai.jpg",
    "name": "Ayam Bakar Mentai + Nasi", "price": 15000},
  {"image": "assets/images/hand-picked/geprek.jpg",
    "name": "Ayam Geprek + Nasi", "price": 17000}
]

db.menu.insert_many(doc)

print("Migration Complete")