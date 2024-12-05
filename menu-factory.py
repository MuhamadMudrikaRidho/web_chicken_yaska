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

print("run menu migration...")

db.menu.drop()
db.carts.drop()
db.wishlists.drop()

doc = [
  {"image": "assets/images/hand-picked/favyasaka.jpg",
    "name": "Ayam Bakar Crispy", "price": 15000, "category" : "Ayam Spicy", "description" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero eum non nihil exercitationem, consequuntur nobis ullam, eveniet laudantium, repudiandae voluptatem ex sunt iusto consectetur cumque?"},
  {"image": "assets/images/hand-picked/chicken.jpg",
    "name": "Chicken + Nasi", "price": 20000, "category" : "Paket Hemat", "description" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam alias vitae eos, corrupti unde ex!"},
  {"image": "assets/images/hand-picked/mentai.jpg",
    "name": "Ayam Bakar Mentai + Nasi", "price": 15000, "category" : "Paket Hemat", "description" : "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sapiente aspernatur facilis a animi, excepturi maiores soluta eaque minima, ipsa totam laboriosam sit iusto fuga mollitia recusandae ullam consequuntur quia facere! Esse eaque ratione quos deleniti sunt. Ad, cumque hic. Porro."},
  {"image": "assets/images/hand-picked/geprek.jpg",
    "name": "Ayam Geprek + Nasi", "price": 17000, "category" : "Paket Hemat", "description" : "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Saepe similique consectetur nihil aspernatur nesciunt possimus corrupti totam minus quod qui? Fugiat accusantium quasi, nostrum nam repellat quae aliquam perferendis corporis?"},
  {"image": "assets/images/hand-picked/selimut.jpg",
    "name": "Ayam Selimut + Nasi", "price": 18000, "category" : "Paket Hemat", "description" : "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Saepe similique consectetur nihil aspernatur nesciunt possimus corrupti totam minus quod qui? Fugiat accusantium quasi, nostrum nam repellat quae aliquam perferendis corporis?"},
  {"image": "assets/images/hand-picked/paket.jpg",
    "name": "Paket Extra Puas", "price": 17000, "category" : "Paket Hemat", "description" : "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Saepe similique consectetur nihil aspernatur nesciunt possimus corrupti totam minus quod qui? Fugiat accusantium quasi, nostrum nam repellat quae aliquam perferendis corporis?"},
  {"image": "assets/images/hand-picked/big.jpg",
    "name": "Chicken Big", "price": 65000, "category" : "Paket Hemat", "description" : "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Saepe similique consectetur nihil aspernatur nesciunt possimus corrupti totam minus quod qui? Fugiat accusantium quasi, nostrum nam repellat quae aliquam perferendis corporis?"},
  {"image": "assets/images/hand-picked/mala.jpg",
    "name": "Ayam Bakar Mala", "price": 20000, "category" : "Paket Hemat", "description" : "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Saepe similique consectetur nihil aspernatur nesciunt possimus corrupti totam minus quod qui? Fugiat accusantium quasi, nostrum nam repellat quae aliquam perferendis corporis?"},
  {"image": "assets/images/hand-picked/sayap.jpg",
    "name": "Paket Winger", "price": 7500, "category" : "Paket Hemat", "description" : "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Saepe similique consectetur nihil aspernatur nesciunt possimus corrupti totam minus quod qui? Fugiat accusantium quasi, nostrum nam repellat quae aliquam perferendis corporis?"}
]

db.menu.insert_many(doc)

print("Migration Complete")