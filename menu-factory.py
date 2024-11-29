import os
from os.path import join, dirname
from dotenv import load_dotenv
from pymongo import MongoClient
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

print("run migration...")

db.menu.drop()

doc = [
  {"image": "assets/images/hand-picked/favyasaka.jpg",
    "name": "Ayam Bakar Crispy", "price": "Rp.15.000"},
  {"image": "assets/images/hand-picked/chicken.jpg",
    "name": "Chicken + Nasi", "price": "Rp.20.000"},
  {"image": "assets/images/hand-picked/mentai.jpg",
    "name": "Ayam Bakar Mentai + Nasi", "price": "Rp.15.000"},
  {"image": "assets/images/hand-picked/geprek.jpg",
    "name": "Ayam Geprek + Nasi", "price": "Rp.17.000"}
]

db.menu.insert_many(doc)

print("Migration Complete")