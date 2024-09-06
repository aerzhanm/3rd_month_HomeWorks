import logging

from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
import os
from config import token


bot = Bot(token=token)
dp = Dispatcher(bot=bot)
admin = ['5060685213']


async def on_sturtup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='бот включен')


@dp.message_handler(commands=['hi'])
async def hi(message: types.Message):
    await message.answer(text='привет, я ваш персональный бот. Чем могу помочь?')


@dp.message_handler(commands=['starts'])
async def start_message(message: types.Message):
    await message.answer(text='вай дос кандай')


@dp.message_handler(commands=['sigma'])
async def sigma(message: types.Message):
    folder = 'media'

    photo_puth = os.path.join(folder, 'img.png')
    with open(photo_puth, 'rb') as photo1:
        await message.answer_photo(photo=photo1)


@dp.message_handler(commands=['sigma.002'])
async def sigma002(message: types.Message):
    folder = 'media'

    photo_tg = os.path.join(folder, 'img_1.png')
    with open(photo_tg, 'rb') as photo2:
        await message.answer_photo(photo=photo2)


@dp.message_handler(commands=['music'])
async def music_handler(message: types.Message):
    folder = 'audio'
    music_name = "treck.mp3"

    music_path = os.path.join(folder, music_name)

    with open(music_path, 'rb') as music:
        await message.answer_audio(music)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await message.answer(int(message.text)**2)

    else:
        await message.answer((message.text))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_sturtup)
