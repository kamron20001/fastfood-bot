from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.course import get_course_keyboards

from loader import dp 


@dp.message_handler(text="Courses📒")
async def course_list(message: types.Message):
    await message.answer(text="Mars It School", reply_markup=get_course_keyboards())