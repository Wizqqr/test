from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from datetime import datetime
from keyboards.choice_kb import quality_service_kb, service_kb
from bookservice.bookservice import BookService
from aiogram import types, F, Router


service_router = Router()
callback_router = Router()


@service_router.callback_query(F.data == 'service')
async def start_service(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(BookService.name)
    await cb.message.answer('What is your name')


@service_router.message(BookService.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookService.number)
    await message.answer(f'Could you tell me your number or instagram {message.text}?')


@service_router.message(BookService.number)
async def process_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(BookService.data)
    await message.answer('When was the last time you entered?')


@service_router.message(BookService.data)
async def process_data(message: Message, state: FSMContext):
    data = message.text
    try:
        datetime.strptime(data, '%d-%m-%Y')
    except ValueError:
        await message.answer('Please write in format DD-MM-YYYY')
        return
    await state.update_data({'date': data})
    await state.set_state(BookService.quality)
    await message.answer('Could you rate our food?', reply_markup=quality_service_kb())


@service_router.message(BookService.quality)
async def process_quality(message: Message, state: FSMContext):
    quality_responses = {
        'excellent': "You've chosen Excellent",
        'good': "You've chosen good",
        'bad': "You've chosen bad",
        'normal': "You've chosen normal"
    }

    async def update_quality(callback: CallbackQuery, state: FSMContext, quality: str):
        await callback.answer(quality_responses[quality])
        await state.update_data({'quality': quality})
        await state.set_state(BookService.cleanable)
        await callback.message.answer(f'You chose "{quality}". Could you rate our service?', reply_markup=service_kb())

    quality = message.text.lower()
    await update_quality(message, state, quality)


@service_router.callback_query(F.data.in_(('excellent', 'good', 'bad', 'normal')))
async def choose_quality(callback: CallbackQuery, state: FSMContext):
    quality = callback.data
    await update_quality(callback, state, quality)


@service_router.callback_query(F.data == 'finish')
async def finish(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Thank you for finishing! \n'
                                  'Would you like to write some comment?')



