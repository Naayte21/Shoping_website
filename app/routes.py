from flask import Blueprint, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

main = Blueprint('main', __name__)
db = SQLAlchemy()

# Product Model (For Database Integration)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), nullable=False)

# Home Route - Loads Products Dynamically
@main.route("/")
def home():
    products = Product.query.all()
    return render_template("index.html", products=products)

# API Route to Fetch Products as JSON
@main.route("/api/products")
def get_products():
    products = Product.query.all()
    product_list = [{"id": p.id, "name": p.name, "price": p.price, "image": p.image} for p in products]
    return jsonify(product_list)
