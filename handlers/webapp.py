from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


async def reply_webapp(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)

    geeks_online = KeyboardButton('Geeks Online', web_app=types.WebAppInfo(url='https://online.geeks.kg'))

    youtube = KeyboardButton('YouTube', web_app=types.WebAppInfo(url='https://www.youtube.com/'))

    keyboard.add(geeks_online, youtube)

    await message.answer(text='Webapp кнопки:', reply_markup=keyboard)


async def inline_webapp(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)

    gitignore_io = InlineKeyboardButton('gitignore.io', web_app=types.WebAppInfo(
        url='https://www.toptal.com/developers/gitignore/'))

    translate = InlineKeyboardButton('Переводчик', web_app=types.WebAppInfo(
        url='https://translate.google.com/?sl=en&tl=ru&op=translate'))

    chat_gpt = InlineKeyboardButton('chat.gpt', web_app=types.WebAppInfo(url='https://chatgpt.com/'))

    kaktus_media = InlineKeyboardButton('kaktus.media', web_app=types.WebAppInfo(url='https://kaktus.media/'))

    keyboard.add(gitignore_io, translate, chat_gpt, kaktus_media)

    await message.answer(text='WebApp кнопки: ', reply_markup=keyboard)

async def webapp(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)

    google = KeyboardButton('Google', web_app=types.WebAppInfo(url='https://www.google.ru/?hl=ru'))
    git = KeyboardButton('GitHub', web_app=types.WebAppInfo(url='https://github.com/'))
    two_books = KeyboardButton('Two Books', web_app=types.WebAppInfo(url='https://2books.su/'))
    twitter = KeyboardButton('Twitter', web_app=types.WebAppInfo(url='https://x.com/?lang=ru'))
    instogram = KeyboardButton('Instogram', web_app=types.WebAppInfo(url='https://www.instagram.com/'))


    keyboard.add(google, git, two_books, twitter, instogram)

    await message.answer(text='Webapp кнопки:', reply_markup=keyboard)



def register_webapp(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands=['reply_webapp'])
    dp.register_message_handler(inline_webapp, commands=['inline_webapp'])
    dp.register_message_handler(webapp, commands=['webapp'])
