import sqlite3

CONN = sqlite3.connect('db/product.sqlite3')

CURSOR = CONN.cursor()


with open("schema.sql", "r") as f:
    sql = f.read()
    
CONN.executescript(sql)
CONN.close()
