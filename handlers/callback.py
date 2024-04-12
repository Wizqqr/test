from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from keyboards.choice_kb import service_kb
from bookservice.bookservice import BookService


callback_router = Router()


@callback_router.callback_query(F.data == 'address')
async def address(callback: types.CallbackQuery):
    await callback.message.answer(text = 'наш адресс : тут близко')


@callback_router.callback_query(F.data == 'phone')
async def phone(callback: types.CallbackQuery):
    await callback.message.answer(text = 'наш телефон : 0996123456789')


quality_responses = {
    'excellent': "You've chosen Excellent",
    'good': "You've chosen good",
    'bad': "You've chosen bad",
    'normal': "You've chosen normal"
}

async def update_quality(callback: types.CallbackQuery, state: FSMContext, quality: str):
    await callback.answer(quality_responses[quality])
    await state.update_data({'quality': quality})
    await state.set_state(BookService.cleanable)
    await callback.message.answer(f'You chose "{quality}". Could you rate our service?', reply_markup=service_kb())

@callback_router.callback_query(F.data.in_(('excellent', 'good', 'bad', 'normal')))
async def choose_quality(callback: types.CallbackQuery, state: FSMContext):
    quality = callback.data
    await update_quality(callback, state, quality)


# @callback_router.callback_query(F.data == 'excellent')
# async def excellent(callback: types.CallbackQuery, state: FSMContext):
#     await callback.answer("You've chosen Excellent")
#     await state.update_data({'quality': 'excellent'})
#     await state.set_state(BookService.cleanable)
#     await callback.message.answer('You chose "excellent". Could you rate our service?', reply_markup=service_kb())
#
#
# @callback_router.callback_query(F.data == 'good')
# async def excellent(callback: types.CallbackQuery, state: FSMContext):
#     await callback.answer("You've chosen good")
#     await state.update_data({'quality': 'good'})
#     await state.set_state(BookService.cleanable)
#     await callback.message.answer('You chose "good". Could you rate our service?', reply_markup=service_kb())
#
#
# @callback_router.callback_query(F.data == 'bad')
# async def excellent(callback: types.CallbackQuery, state: FSMContext):
#     await callback.answer("You've chosen bad")
#     await state.update_data({'quality': 'bad'})
#     await state.set_state(BookService.cleanable)
#     await callback.message.answer('You chose "bad". Could you rate our service?', reply_markup=service_kb())
#
#
# @callback_router.callback_query(F.data == 'normal')
# async def excellent(callback: types.CallbackQuery, state: FSMContext):
#     await callback.answer("You've chosen normal")
#     await state.update_data({'quality': 'normal'})
#     await state.set_state(BookService.cleanable)
#     await callback.message.answer('You chose "normal". Could you rate our service?', reply_markup=service_kb())


@callback_router.callback_query(F.data == 'finish')
async def finish(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Thank you for finishing! \n'
                                  'Would you like to write some comment?')


