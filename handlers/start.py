import services
from bot import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    service = services.AuthService()
    await service.add_user(user_id=message.from_user.id, user_name=message.from_user.username)
    await message.answer(text='hello there')
