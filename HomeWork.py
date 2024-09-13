import logging
from aiogram.utils import executor
from config import bot, dp, admin
from handlers import commands, echo, quiz, game, FSM_store, FSM_registration
from buttons import start
from aiogram import types


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='бот включен', )


@dp.message_handler(commands=['start'])
async def hi(message: types.Message):
    await message.answer(text='привет, я ваш персональный бот. Чем могу помочь?',
                         reply_markup=start
                         )


commands.register_commands(dp)
quiz.register_quiz(dp)
game.register_game(dp)
FSM_registration.register_fsm(dp)
FSM_store.register_store(dp)

echo.register_echo(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
