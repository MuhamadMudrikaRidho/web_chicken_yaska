import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    jsonify
)

from pymongo import MongoClient
from bson import ObjectId

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route("/")
def home() :
  return render_template('index.html', login=False)

@app.route("/menu")
def menu() :
  return render_template('menu.html', login=False)

@app.route('/about')
def about() :
  return render_template('about.html', login=False)

port=5000
debug=True

if __name__ == "__main__" :
  app.run('0.0.0.0', port=port, debug=debug)