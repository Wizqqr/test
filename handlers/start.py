from aiogram.filters import Command
from aiogram import Router, types
from keyboards.start_kb import start_kb


start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    text = f'привет {message.from_user.full_name}\n' \
           f'Я бот для заказа пиццы.\n' \
           f'Ниже вы можете выбрать раздел используя кнопки'
    await message.answer(text, reply_markup=start_kb())




