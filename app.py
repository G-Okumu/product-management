from flask import Flask, request, jsonify
from flask_migrate import Migrate

from config import db

from models.category import Category
from models.product import Product




# instantiate the flask project
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///product_management.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def test():
    return ("Program is running well")


@app.route("/categories", methods=["POST"])
def creat_category():
    incoming_data = request.get_json()
    
    name = incoming_data.get("name")
    size = incoming_data.get("size")
    
    
    # validations
    
    if not isinstance(name, str):
        return jsonify({"error": "Name must be a string or required"}), 400
    
    if type(size) is not int or size < 1:
        return jsonify({"error": "Name must be an int  or greater than 0"}), 400

            
    category = Category(
       name=name,
       size=size
    )
        

    
    db.session.add(category)
    db.session.commit()
    
    return jsonify({"message": "Category created successfully", "id": category.id, "name": category.name}), 201


@app.route("/products", methods=["POST"])
def creat_product():
    incoming_data = request.get_json()
    
    product = Product(
        name=incoming_data["name"],
        price=incoming_data["price"],
        measurement_unit=incoming_data["measurement_unit"],
        category_id=incoming_data["category_id"]
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify({"message": "Product created successfully", "id": product.id, "name": product.name}), 201


@app.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    
        
    all_categs = []
    
    for categ in categories:
        all_categs.append({"name": categ.name, "size": categ.size, "products": [{"product name": p.name, "product price": p.price} for p in categ.products ]  })
        
    print(all_categs)
    
    return jsonify({"message": "All Categories", "categories": all_categs})



# Tomorrows objectives

# 1. Validation and constraints => your writing your method checks, constraints, you leave it for the db
# 2. Serialization

if __name__ == "__main__":
    app.run()
