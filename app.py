from flask import Flask
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



if __name__ == "__main__":
    app.run()
