from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
).add(
    KeyboardButton('/starts'),
    KeyboardButton('/mem'),
    KeyboardButton('/sigma.002'),
    KeyboardButton('/garri_potter'),
    KeyboardButton('/music'))
