from decouple import config
from aiogram import Bot, Dispatcher

token = config('TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot=bot)
admin = ['5060685213']

