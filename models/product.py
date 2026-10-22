
class Product:
    
    def __init__(self, name: str, price: float, quantity: int, measurement_unit: str, category_id: int,id: int = None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.measurement_unit = measurement_unit
        self.category_id = category_id
        
        
    @property
    def quantity(self) -> int:
        return self._quantity
    

    @quantity.setter
    def quantity(self, new_val: int) -> None:
        if new_val < 0:
            raise ValueError('Quantity starts from 1')
        else:
            self._quantity = new_val