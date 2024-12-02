from config import DevelopmentConfig
from flask import Flask
from pymongo import MongoClient
import os
import bcrypt

app = Flask(__name__)

ENV = os.getenv("FLASK_ENV", "development")

if ENV == "development":
    app.config.from_object(DevelopmentConfig)

client = MongoClient(app.config['MONGODB_URI'])
db = client[app.config['DB_NAME']]

print("run user migration...")

db.users.drop()

buyerPass = bcrypt.hashpw("buyer".encode('utf-8'), bcrypt.gensalt())
adminPass = bcrypt.hashpw("admin".encode('utf-8'), bcrypt.gensalt())

doc = [
  {
    "name" : "Buyer",
    "username" : "buyer",
    "email" : "buyer@gmail.com",
    "password" : buyerPass.decode('utf-8'),
    "isAdmin" : False
  },
  {
      "name" : "Admin",
      "username" : "username",
      "email" : "admin@gmail.com",
      "password" : adminPass.decode('utf-8'),
      "isAdmin" : True
  }
]

db.users.insert_many(doc)

print("Migration Complete")