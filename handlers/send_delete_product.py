import sqlite3
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.dispatcher.filters import Text
from config import admin

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM products p 
    INNER JOIN products_details pd ON p.product_id = pd.product_id  
    """).fetchall()
    conn.close()
    return products



def delete_product(product_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM products WHERE product_id + ?", (product_id,))
    conn.commit()
    conn.close()


async def start_sending_products(message: types.Message):
    products = fetch_all_products()

    if products:
        for product in products:
            caption = (f"Артикул - {product['product_id']}\n"
                       f"Название товара - {product['name_product']}\n"
                       f"Информация о товаре - {product['info_product']}\n"
                       f"Категория - {product['category']}\n"
                       f"Коллекция - {product['collection']}\n"
                       f"Размер - {product['size']}\n"
                       f"Цена - {product['price']} сом\n")

            await message.answer_photo(photo=product['photo'], caption=caption)
    else:
        await message.answer("Товары не найдены!")

async def start_sending_products_for_delete(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button = InlineKeyboardButton('Все_товары', callback_data='show_all_delete')
    keyboard.add(button)

    await message.answer('Нажмите на кнопку, чтобы увидеть все товары с возможностью удаления!',
                         reply_markup=keyboard)



async def show_all_products_for_delete(callback_query: types.CallbackQuery):
    products = fetch_all_products()

    if products:
        for product in products:
            caption = (f"Артикул - {product['product_id']}\n"
                       f"Название товара - {product['name_product']}\n"
                       f"Информация о товаре - {product['info_product']}\n"
                       f"Категория - {product['category']}\n"
                       f"Коллекция - {product['collection']}\n"
                       f"Размер - {product['size']}\n"
                       f"Цена - {product['price']} сом\n")

            delete_product_markup = InlineKeyboardMarkup(resize_keyboard=True)
            delete_product_button = InlineKeyboardButton('Удалить', callback_data=f'delete_{product["product_id"]}')
            delete_product_markup.add(delete_product_button)

            await callback_query.message.answer_photo(photo=product['photo'], caption=caption, reply_markup=delete_product_markup)
    else:
        await callback_query.message.answer("Товары не найдены!")


async def delete_product_callback(callback_query: types.CallbackQuery):
    product_id = int(callback_query.data.split('_')[1])

    # Проверка прав администратора
    if callback_query.from_user.id not in admin:
        await callback_query.answer("У вас нет прав для удаления товара!", show_alert=True)
        return

    delete_product(product_id)

    await callback_query.answer('Товар удален!')

    if callback_query.message.photo:
        new_caption = 'Товар был удалён. \nОбновите список!'

        photo_404 = open('media/img_404.png', 'rb')

        await callback_query.message.edit_media(
            InputMediaPhoto(media=photo_404, caption=new_caption))
    else:
        await callback_query.message.edit_text('Товар был удалён. \nОбновите список!')


def register_send_delete_product(dp: Dispatcher):
    dp.register_message_handler(start_sending_products, commands=['send_products'])
    dp.register_message_handler(start_sending_products_for_delete, commands=['send_products_delete'])
    dp.register_callback_query_handler(show_all_products_for_delete, Text(equals='show_all_delete'))
    dp.register_callback_query_handler(delete_product_callback, Text(startswith='delete_'))