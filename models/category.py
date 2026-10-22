class Category():
    
    def __init__(self, name: str, size: int, type: str, products: list = None,id: int = None):
        self.id  = id
        self.name = name
        self.size = size
        self.type = type
        self.products = products if products is not None else [] # one to many. One category record associated with many product records