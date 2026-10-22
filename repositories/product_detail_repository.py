from models.product_detail import ProductDetail

from config import CONN, CURSOR

class ProductDetailRepository:
    
    def create_product_detail(self, prodDe: ProductDetail):
        sql = """
            insert into product_details (product_id, description, warranty_year) values (?, ?, ?)
        """

        CURSOR.execute(sql, (prodDe.product_id, prodDe.description, prodDe.warranty_year))
        
        CONN.commit()