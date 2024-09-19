CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    product_id VARCHAR(255),
    photo TEXT
    )
"""

INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (name_product, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""

CREATE_TABLE_PRODUCT_DETAIL = '''
CREATE TABLE IF NOT EXISTS product_detailes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_id VARCHAR(255),
category VARCHAR(255),
info_product VARCHAR(255)
)
'''

INSERT_PRODUCT_DETAIL = '''
INSERT INTO product_detailes(product_id, category, info_product)
 VALUES (?, ?, ?)
'''

CREATE_TABLE_PRODUCT_COLLECTION = '''
CREATE TABLE IF NOT EXISTS product_collection(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_id VARCHAR(255),
collection VARCHAR(255)
)
'''

INSERT_INTO_PRODUCT_COLLECTION = '''
INSERT INTO product_collection(product_id, collection)
VALUES (?, ?)'''