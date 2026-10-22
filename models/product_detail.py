class ProductDetail():
    def __init__(self, product_id: int, description: str, warranty_year: int, id: int = None):
        self.id = id
        self.product_id = product_id
        self.description = description
        self.warranty_year = warranty_year
        