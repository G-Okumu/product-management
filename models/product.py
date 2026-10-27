from config import db

class Product(db.Model):
    
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4), nullable=False)
    price = db.Column(db.Float)
    measurement_unit = db.Column(db.String(10))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id")) # one to many, where relationship is done
    __table_args__ = (db.CheckConstraint("price >= 1", name="product_price_must_be_greater_than_one"),)

    
    category = db.relationship("Category", back_populates="products") # this is where relationship attribute connection is done
    
    # constraint
    
    
    
    
    # def __init__(self, name: str, price: float, quantity: int, measurement_unit: str, category_id: int,id: int = None):
    #     self.id = id
    #     self.name = name
    #     self.price = price
    #     self.quantity = quantity
    #     self.measurement_unit = measurement_unit
    #     self.category_id = category_id
        
        
    # @property
    # def quantity(self) -> int:
    #     return self._quantity
    

    # @quantity.setter
    # def quantity(self, new_val: int) -> None:
    #     if new_val < 0:
    #         raise ValueError('Quantity starts from 1')
    #     else:
    #         self._quantity = new_val