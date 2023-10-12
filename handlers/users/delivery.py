from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(text="menu")
async def get_menu(message: types.Message):
    await message.answer(f"CHoose any from menu !")