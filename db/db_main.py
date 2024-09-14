import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
c = db.cursor()


async def sql_create():
    if db:
        print('База данных подключена!')

    c.execute(queries.CREATE_TABLE_PRODUCTS)
    db.commit()


async def sql_insert_products(name_product, size, price, product_id, photo):
    c.execute(queries.INSERT_PRODUCTS, (
        name_product,
        size,
        price,
        product_id,
        photo
    )


              )
