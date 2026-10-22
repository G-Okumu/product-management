from models.product import Product

from config import CONN, CURSOR
class ProductRepository:    
    
    def create_product(self, product: Product):
        
        sql = """ 
        
        insert into products (name, price, quantity, measurement_unit)  values (?, ?, ?, ?)
        
        """
        
        CURSOR.execute(sql, (product.name, product.price, product.quantity, product.measurement_unit, product.category_id))
        CONN.commit()
        
        return {"message": "product added successfully"}
    
    def get_product_by_id(self, product_id: int):
        
        sql = """
        
        select id, name, price, quantity, measurement_unit, category_id from products where id = ?
        
        """
        
        CURSOR.execute(sql, (product_id,))
        
        found_item = CURSOR.fetchone()
        
        
        print(f"in repository folder {found_item}")
        
        if found_item is None:
            return None
        
        return Product(
            id=found_item[0],
            name=found_item[1],
            price=found_item[2],
            quantity=found_item[3],
            measurement_unit=found_item[4],
            category_id=found_item[5]
        )
        
        
    def get_all_products_with_their_details(self):
        sql = """
        
        select p.name, p.price, p.quantity, p.measurement_unit, pd.description, pd.warranty_year from products p left join product_details pd on p.id = pd.product_id
        
        """
        
        CURSOR.execute(sql)
        
        return CURSOR.fetchall()
