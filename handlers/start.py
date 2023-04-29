from bot import bot, dp
from aiogram.types import Message

@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text='hello there')