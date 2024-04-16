from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from datetime import datetime
from keyboards.choice_kb import quality_service_kb, service_kb
from bookservice.bookservice import BookService
from aiogram import types, F, Router
from bot import database


service_router = Router()


@service_router.callback_query(F.data == 'service')
async def start_service(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(BookService.name)
    await cb.message.answer('What is your name')


@service_router.message(BookService.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookService.number)
    await message.answer(f'Could you tell me your number or Instagram {message.text}?')



@service_router.message(BookService.number)
async def process_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(BookService.date)
    await message.answer('When was the last time you entered?')



@service_router.message(BookService.date)
async def process_date(message: Message, state: FSMContext):
    date = message.text
    try:
        datetime.strptime(date, '%d-%m-%Y')
    except ValueError:
        await message.answer('Please write in format DD-MM-YYYY')
        return
    await state.update_data(date=date)
    await state.set_state(BookService.quality)
    await message.answer('Could you rate our food?', reply_markup=quality_service_kb())


@service_router.message(BookService.last)
async def process_last_state(message: Message, state: FSMContext):
    await state.update_data(last=message.text)
    data = await state.get_data()
    print(data)
    await database.execute(
            'INSERT INTO service (name, number, date, quality, cleanable, last) VALUES (?, ?, ?, ?, ?, ?)',
            (data['name'], data['number'], data['date'], data['quality'], data['cleanable'], data['last'])
        )
    await message.answer('Thank you! Your data has been processed.')
    await state.clear()

