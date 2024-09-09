from aiogram import types, Dispatcher
import os
from buttons import start


async def hi(message: types.Message):
    await message.answer(text='привет, я ваш персональный бот. Чем могу помочь?',
                         )


async def sigma(message: types.Message):
    folder = 'media'

    photo_path = os.path.join(folder, 'img.png')
    with open(photo_path, 'rb') as photo1:
        await message.answer_photo(photo=photo1)


async def sigma002(message: types.Message):
    folder = 'media'

    photo_tg = os.path.join(folder, 'img_1.png')
    with open(photo_tg, 'rb') as photo2:
        await message.answer_photo(photo=photo2)


async def garry_potter(message: types.Message):
    folder = 'media'
    photo_tg = os.path.join(folder, 'поттер.jpg')
    with open(photo_tg, 'rb') as photo3:
        await message.answer_photo(photo=photo3)


async def music_handler(message: types.Message):
    folder = 'audio'
    music_name = "treck.mp3"

    music_path = os.path.join(folder, music_name)

    with open(music_path, 'rb') as music:
        await message.answer_audio(music)


async def starts(message: types.Message):
    await message.answer(text='вай дос кандай')


def register_commands(dp: Dispatcher):
    dp.register_message_handler(hi, commands="hi"),
    dp.register_message_handler(sigma, commands="sigma"),
    dp.register_message_handler(sigma002, commands="sigma002"),
    dp.register_message_handler(music_handler, commands="music_handler"),
    dp.register_message_handler(starts, commands="start"),
