from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


async def quiz_1(message: types.Message):
    quiz_button = InlineKeyboardMarkup()
    button_quiz1 = InlineKeyboardButton('дальше...',
                                        callback_data='button')
    quiz_button.add(button_quiz1)

    question = 'Math or Phisick'
    answer = ['Math', 'Phisick', 'History']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='вай брааат!',
        open_period=30,
        reply_markup=quiz_button
    )


async def quiz_2(call: types.CallbackQuery):
    quiz_button = InlineKeyboardMarkup()
    button_quiz = InlineKeyboardButton('дальше...',
                                       callback_data='button_1')

    quiz_button.add(button_quiz)
    q = 'Месси или Роналдо'
    answer = ['Месси', 'Роналдо', 'Неймар']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=q,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='СУУУУ!',
        open_period=30,
        reply_markup=quiz_button
    )


async def quiz_3(call: types.CallbackQuery):
    quiz_button = InlineKeyboardMarkup()
    button_quiz = InlineKeyboardButton('дальше...',
                                       callback_data='button_2')

    quiz_button.add(button_quiz)
    q = 'америка или испания'
    answer = ['америка', 'испания', 'дом']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=q,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='дом!',
        open_period=30,
        reply_markup=quiz_button
    )


async def quiz_4(call: types.Message):
    quiz_button = InlineKeyboardMarkup()
    button_quiz = InlineKeyboardButton('дальше...',
                                       callback_data='button_3')

    quiz_button.add(button_quiz)
    q = '10 баллов или 5?'
    answer = ['10', '5', '8']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=q,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='10',
        open_period=30,
        reply_markup=button_quiz
    )


def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz']),
    dp.register_callback_query_handler(quiz_2, text='button'),
    dp.register_callback_query_handler(quiz_3, text='button_1'),
    dp.register_callback_query_handler(quiz_4, text='button_2')
