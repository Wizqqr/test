from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
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


@callback_router.callback_query(F.data == 'gender_M')
async def gender_M(callback: types.CallbackQuery):
    await callback.message.answer(text = 'Вы выбрали мужской пол')

@callback_router.callback_query(F.data == 'gender_W')
async def gender_W(callback:types.CallbackQuery):
    await callback.message.answer(text = 'Вы выбрали женский пол')


@callback_router.callback_query(F.data == 'excellent')
async def excellent(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("You've chosen Excellent")
    await state.update_data({'quality': 'excellent'})
    await state.set_state(BookService.cleanable)
    await callback.message.answer('You chose "excellent". Could you rate our service?', reply_markup=service_kb())


@callback_router.callback_query(F.data == 'good')
async def excellent(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("You've chosen good")
    await state.update_data({'quality': 'good'})
    await state.set_state(BookService.cleanable)
    await callback.message.answer('You chose "good". Could you rate our service?', reply_markup=service_kb())


@callback_router.callback_query(F.data == 'bad')
async def excellent(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("You've chosen bad")
    await state.update_data({'quality': 'bad'})
    await state.set_state(BookService.cleanable)
    await callback.message.answer('You chose "bad". Could you rate our service?', reply_markup=service_kb())


@callback_router.callback_query(F.data == 'normal')
async def excellent(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("You've chosen normal")
    await state.update_data({'quality': 'normal'})
    await state.set_state(BookService.cleanable)
    await callback.message.answer('You chose "normal". Could you rate our service?', reply_markup=service_kb())


@callback_router.callback_query(F.data == 'finish')
async def finish(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Thank you for finishing! \n'
                                  'Would you like to write some comment?')


