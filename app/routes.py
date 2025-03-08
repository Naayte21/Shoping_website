from flask import Blueprint, render_template, jsonify
from .models import db, Product  # Import db from models

main = Blueprint('main', __name__)

@main.route("/")
def home():
    products = Product.query.all()
    return render_template("index.html", products=products)

@main.route("/api/products")
def get_products():
    products = Product.query.all()
    product_list = [{"id": p.id, "name": p.name, "price": p.price, "image": p.image} for p in products]
    return jsonify(product_list)
