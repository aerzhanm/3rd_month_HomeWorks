import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print('База данных подключена!')

    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    cursor.execute(queries.CREATE_TABLE_PRODUCT_DETAIL)
    cursor.execute(queries.CREATE_TABLE_PRODUCT_COLLECTION)
    db.commit()


async def sql_insert_products(name_product, size, price, product_id, photo):
    with sqlite3.connect('db/store.sqlite3') as db_with:
        cursor_with = db_with.cursor()
        cursor_with.execute(queries.INSERT_PRODUCTS_QUERY, (
            name_product,
            size,
            price,
            product_id,
            photo
        ))
        db_with.commit()


async def products_details(product_id, category, info_product):
    with sqlite3.connect('db/store.sqlite3') as db_with:
        cursor_with = db_with.cursor()
        cursor_with.execute(queries.INSERT_PRODUCT_DETAIL, (
            product_id, category, info_product
        ))
        db_with.commit()


async def products_collection(product_id, collection):
    with sqlite3.connect('db/store.sqlite3') as db_with:
        cursor_with = db_with.cursor()
        cursor_with.execute(queries.INSERT_INTO_PRODUCT_COLLECTION, (
            product_id, collection
        ))
        db_with.commit()
