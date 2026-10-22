from repositories.product_repository import ProductRepository
from repositories.category_repository import CategoryRepository
from repositories.product_detail_repository import ProductDetailRepository

from models.product import Product
from models.category import Category
from models.product_detail import ProductDetail


product_repo = ProductRepository()
category_repo = CategoryRepository()
details_repo = ProductDetailRepository()


# one 2 one : product and product detail

product_id = 1

searched_product = product_repo.get_product_by_id(product_id)

if searched_product is None:
    print(f"Product with ID {product_id} not found")

else:
    product_detail = ProductDetail(
        searched_product.id,
        "This is the description of this product",
        2
    )

    result = details_repo.create_product_detail(product_detail)

    print("Product details added:", result)


all_products = product_repo.get_all_products_with_their_details()

for product in all_products:
    print("\nProduct:", product)

    if product.details is not None:
        print("Details:", product.details)
    else:
        print("No details available")



# one to many, that is category -> products

category_id = 1

searched_category = category_repo.get_category_by_id(category_id)

if searched_category is None:
    print(f"Category with ID {category_id} not found")

else:
    product = Product(
        "Beef",
        45,
        2,
        "Kgs",
        category_id=searched_category.id
    )

    result = product_repo.create_product(product)

    print("Product added to category:", result)


# Retrieve the category and its products
category_with_products = category_repo.get_category_with_products(category_id)

if category_with_products is None:
    print(f"Category with ID {category_id} not found")

else:
    print("\nCategory:", category_with_products.name)

    for product in category_with_products.products:
        print(product)