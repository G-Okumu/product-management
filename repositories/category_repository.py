from config import CONN, CURSOR
from models.category import Category
from models.product import Product

from typing import List


class CategoryRepository:

    def create_category(self, category: Category) -> Category:
        sql = """
            INSERT INTO categories (name, size, type)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(
            sql,
            (category.name, category.size, category.type)
        )

        category.id = CURSOR.lastrowid
        CONN.commit()

        return category

    def get_category_by_id(self,category_id: int) -> Category:


        CURSOR.execute(""" SELECT id, name, size, type FROM categories WHERE id = ? """, (category_id,))
        row = CURSOR.fetchone()

        if row is None:
            return None

        return Category(
            id=row[0],
            name=row[1],
            size=row[2],
            type=row[3]
        )

    def get_category_with_products(self,category_id: int) -> Category:
        sql = """
            SELECT
                c.id,
                c.name,
                c.size,
                c.type,
                p.id,
                p.name,
                p.price,
                p.quantity,
                p.measurement_unit,
                p.category_id
            FROM categories AS c
            LEFT JOIN products AS p
                ON c.id = p.category_id
            WHERE c.id = ?
            ORDER BY p.id
        """

        CURSOR.execute(sql, (category_id,))
        rows = CURSOR.fetchall()

        if not rows:
            return None

        first = rows[0]

        category = Category(
            id=first[0],
            name=first[1],
            size=first[2],
            type=first[3]
        )

        for row in rows:
            if row[4] is None:
                continue

            product = Product(
                id=row[4],
                name=row[5],
                price=row[6],
                quantity=row[7],
                measurement_unit=row[8],
                category_id=row[9]
            )

            category.products.append(product)

        return category

    def get_all_categories_with_products(self) -> List[Category]:
        CURSOR.execute("""
                       
                       SELECT
                        c.id,
                        c.name,
                        c.size,
                        c.type,
                        p.id,
                        p.name,
                        p.price,
                        p.quantity,
                        p.measurement_unit,
                        p.category_id
                    FROM categories AS c
                    LEFT JOIN products AS p
                        ON c.id = p.category_id
                    ORDER BY c.id, p.id
                    
                    """)
        rows = CURSOR.fetchall()

        categories_by_id = {}

        for row in rows:
            category_id = row[0]

            if category_id not in categories_by_id:
                categories_by_id[category_id] = Category(
                    id=row[0],
                    name=row[1],
                    size=row[2],
                    type=row[3]
                )

            if row[4] is not None:
                product = Product(
                    id=row[4],
                    name=row[5],
                    price=row[6],
                    quantity=row[7],
                    measurement_unit=row[8],
                    category_id=row[9]
                )

                categories_by_id[category_id].products.append(product)

        return list(categories_by_id.values())