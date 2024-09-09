import logging
from aiogram.utils import executor
from config import bot, dp, admin
from handlers import commands, echo
from buttons import start



async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='бот включен', reply_markup=start)


commands.register_commands(dp)
echo.register_echo(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
