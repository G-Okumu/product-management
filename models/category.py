from config import db

class Category(db.Model):
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    size = db.Column(db.Integer)
    
    products = db.relationship("Product", back_populates="category")
    
    # def __init__(self, name: str, size: int, type: str, products: list = None,id: int = None):
    #     self.id  = id
    #     self.name = name
    #     self.size = size
    #     self.type = type
    #     self.products = products if products is not None else [] # one to many. One category record associated with many product records