from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from aiogram.contrib.middlewares.logging import LoggingMiddleware


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
dp.middleware.setup(LoggingMiddleware())

