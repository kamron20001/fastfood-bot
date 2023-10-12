from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboard.default.start_keyboard import get_start_keyboards

from loader import dp 

@dp.message_handler(text="About Us")
async def about(message : types.Message):
    photo = "https://avatars.mds.yandex.net/get-altay/998620/2a00000185bedb0cfe606686bf9d0f3c6bac/L_height"
    