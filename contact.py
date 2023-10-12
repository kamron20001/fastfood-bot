from aiogram import types

from loader import dp, bot
from states.contacts import ContactState
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="Menyu")
async def menyu(message: types.Message):
    await message.answer("Enter your phone !")
    await ContactState.phone.set()
    
    
    
@dp.message_handler(states=ContactState.phone)
async def contact(message: types. state: FSMContext)