from flask import Blueprint, render_template, current_app, request, session, url_for, redirect, jsonify, flash
from bson import ObjectId
from datetime import datetime

menu_bp = Blueprint("menu", __name__, url_prefix="/menu")

def convert_ids_to_strings(document):
    if isinstance(document, list):
        return [convert_ids_to_strings(item) for item in document]
    elif isinstance(document, dict):
        return {
            key: str(value) if isinstance(value, ObjectId) else convert_ids_to_strings(value)
            for key, value in document.items()
        }
    else:
        return document

@menu_bp.route("/")
def home():
    db = current_app.config['DB']
    sort_option = request.args.get('sort', 'default') 

    if sort_option == 'price_asc':
        menus = list(db.menu.find({}).sort('price', 1))
    elif sort_option == 'price_desc':
        menus = list(db.menu.find({}).sort('price', -1)) 
    else:
        menus = list(db.menu.find({})) 

    user = "hehe"
    if 'username' in session : 
        user = session['username']
    isWishlisted = False

    for menu in menus:
        menu['_id'] = str(menu['_id'])
        if db.wishlists.find_one({'menu_id' : menu['_id'], 'user' : user}) : 
            isWishlisted = True

    return render_template("menu.html", menus=menus, current_sort=sort_option, isWishlisted=isWishlisted)

@menu_bp.route("/<id>")
def detail(id):
    db = current_app.config['DB']
    menu = db.menu.find_one({"_id": ObjectId(id)})
    if not menu : 
        return jsonify({"status" : "error", "message" : "menu tidak ditemukan"}), 404
    reviews = list(db.reviews.find({"menu_id" : id}))
    total_reviews = db.reviews.count_documents({"menu_id" : id})

    converted_reviews = convert_ids_to_strings(reviews)
    
    reviewed = False
    user = "hehe"
    login_user = []
    if 'username' in session : 
        login_user = db.users.find_one({'username' : session['username']})
        user = login_user['username']
        for review in converted_reviews :
            if review['user']['username'] == user :
                reviewed = True
    
    isWishlisted = False

    if db.wishlists.find_one({'menu_id' : menu['_id'], 'user' : user}) : 
            isWishlisted = True

    if not menu:
        return "Menu not found", 404

    menu['_id'] = str(menu['_id'])
    menu['price'] = menu['price']
    count_price = menu['price'] + 3000
    
    return render_template('detail-menu.html',reviewed=reviewed, total_reviews=total_reviews, reviews=converted_reviews, user=login_user, menu=menu, count_price=count_price, isWishlisted=isWishlisted)

@menu_bp.route('/submit-review/<menu_id>', methods=["POST"])
def store_review(menu_id) :

    if 'username' not in session : 
        return redirect(url_for('auth.login'))

    db = current_app.config['DB']
    user = request.form.get('username')
    user_data = db.users.find_one({"username" : user})

    menu_id = menu_id
    name = request.form.get('name')
    email = request.form.get('email')
    review = request.form.get('review')
    rating = request.form.get('rating')
    date = datetime.now().strftime("%B %d, %Y")

    if not rating :
        flash("Mohon masukkan nilaimu, untuk menilai seberapa puas kamu dengan menu ini", "danger")
        return redirect(f'/menu/{menu_id}')

    doc = {
        "menu_id" : menu_id,
        "name" : name,
        "email" : email,
        "user" : user_data,
        "review" : review,
        "rating" : int(rating),
        "date" : date
    }

    db.reviews.insert_one(doc)
    flash("Ulasanmu tersimpan. Terimakasih atas ulasan yang diberikan", "success")
    return redirect(f'/menu/{menu_id}')

@menu_bp.route('/average-rating/<menu_id>')
def average_rating(menu_id) :
    db = current_app.config["DB"]

    reviews = list(db.reviews.find({"menu_id" : menu_id}))
    rating_reviews = []
    for review in reviews :
        review['_id'] = str(review['_id'])
        rating_reviews.append(review['rating'])

    average = sum(rating_reviews) / len(reviews)
    return jsonify({'average': average, 'total_reviews': len(reviews)})
    
@menu_bp.route('/update-review/<review_id>/<menu_id>', methods=["POST"])
def update_review(review_id, menu_id) : 
    db = current_app.config['DB']

    user = request.form.get('username')
    receive_review = request.form.get('review')
    rating = int(request.form.get('rating'))
    user_data = db.users.find_one({"username" : user})
    user_data['_id'] = str(user_data['_id'])
    date = datetime.now().strftime("%B %d, %Y")

    db.reviews.update_one({"_id" : ObjectId(review_id)}, {"$set" : {
        "user" : user_data,
        "review" : receive_review,
        "rating" : rating,
        "date" : date,
        "isEdit" : "edited"
    }})

    flash("Ulasanmu telah diperbarui! Terimakasih atas ulasan yang diberikan", "success")
    return redirect(f'/menu/{menu_id}')
    