import logging
from aiogram.utils import executor
from buttons import start_test
from config import bot, dp, admin
from handlers import (commands, echo, quiz, FSM_registration,
                      FSM_store, webapp, admin_group_2, admin_group,
                      adminnjnjn, send_products, send_delete_product)
from db import db_main
import buttons


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!",
                               reply_markup=buttons.start)
        await db_main.sql_create()


commands.register_commands(dp)
quiz.register_quiz(dp)
FSM_registration.register_fsm(dp)
FSM_store.register_store(dp)
webapp.register_webapp(dp)
send_products.register_send_products(dp)
send_delete_product.register_send_delete_product(dp)

admin_group_2.register_admin_group(dp)
admin_group.register_admin_group(dp)
adminnjnjn.register_admin(dp)


echo.register_echo(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
