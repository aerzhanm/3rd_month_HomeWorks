from aiogram import types, Dispatcher
from config import bot, admin

hello = ['hello', 'hi', 'привет', 'кандай', 'здарово']

async def hello_words(message: types.Message):
    message_text = message.text.lower()
    for words in hello:
        if words in message_text:
            await message.answer(f'Здравствуйте, вас прветствует бот Мистера Эржана')

def register_admin(dp: Dispatcher):
    dp.register_message_handler(hello_words)