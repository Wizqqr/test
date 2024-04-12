from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from datetime import datetime
from keyboards.choice_kb import quality_service_kb
from bookservice.bookservice import BookService


service_router = Router()





@service_router.callback_query(F.data == 'service')
async def start_service(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(BookService.name)
    await cb.message.answer('What is your name')


@service_router.message(BookService.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookService.number)
    await message.answer(f'Could you tell me your number or instagram {message.text}?')


@service_router.message(BookService.number)
async def process_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(BookService.data)
    await message.answer('When was the last time you entered?')


@service_router.message(BookService.data)
async def process_data(message: types.Message, state: FSMContext):
    data = message.text
    try:
        datetime.strptime(data, '%d-%m-%Y')
    except ValueError:
        await message.answer('Please write in format DD-MM-YYYY')
        return
    await state.update_data({'date': data})
    await state.set_state(BookService.quality)
    await message.answer('Could you rate our food?', reply_markup=quality_service_kb())


