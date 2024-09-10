'''from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
).add(
    KeyboardButton('/starts'),
    KeyboardButton('/mem'),
    KeyboardButton('/sigma.002'),
    KeyboardButton('/garri_potter'),
    KeyboardButton('/music')
)'''

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ===============================================================

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

start_buttons = KeyboardButton('/sigma')
mem_buttons = KeyboardButton('/sigma002')
mem_all_buttons = KeyboardButton('/potter')
music_buttons = KeyboardButton('/music')

start.add(start_buttons, mem_buttons, mem_all_buttons,
          music_buttons)

# ===============================================================

start_test = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
).add(
    KeyboardButton('/start'),
    KeyboardButton('/mem'),
    KeyboardButton('/mem_all'),
    KeyboardButton('/music')
)

# ===============================================================

start_test_1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
)

start_test_1.add(
    KeyboardButton('/start'),
    KeyboardButton('/mem'),
    KeyboardButton('/mem_all'),
    KeyboardButton('/music')
)

# ===============================================================
