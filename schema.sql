CREATE TABLE IF NOT EXISTS products (id integer PRIMARY KEY AUTOINCREMENT, name TEXT, price FLOAT, quantity integer, measurement_unit TEXT);

CREATE TABLE IF NOT EXISTS categories (id integer PRIMARY KEY AUTOINCREMENT, name TEXT, size integer, type TEXT);

CREATE TABLE IF NOT EXISTS product_details (id integer PRIMARY KEY AUTOINCREMENT, product_id integer not null, description TEXT, warranty_year integer, FOREIGN KEY(product_id) REFERENCES products(id));

-- CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,size INTEGER,type TEXT);

-- ALTER TABLE products ADD COLUMN  IF NOT EXISTS category_id INTEGER  REFERENCES categories(id);,-- run this mara jamo, hehe