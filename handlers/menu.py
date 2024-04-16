from aiogram import Router, types, F
from keyboards.menu_kb import menu_kb


menu_router = Router()


@menu_router.callback_query(F.data == 'menu')
async def menu(callback: types.CallbackQuery):
    await callback.message.answer(text = 'список наших блюд', reply_markup=menu_kb())


@menu_router.message(lambda message: message.text in ["первые блюда", "вторые блюда", "десерт", "напитки"])
async def handle_menu(message: types.Message):
    if message.text == 'первые блюда':
        await message.answer("Вы выбрали раздел 'первые блюда'. Вот наше меню первых блюд:\n"
                             "Щи\n"
                             "Бульоны\n"
                             "Супы\n"
                             "Солянки")
    elif message.text == 'вторые блюда':
        await message.answer("Вы выбрали раздел 'вторые блюда'. Вот наше меню вторых блюд:\n"
                             "Котлеты\n"
                             "Плов\n"
                             "Манты\n"
                             "Пицца\n"
                             "Рис")
    elif message.text == 'десерт':
        await message.answer("Вы выбрали раздел 'десерт'. Вот наше меню десертов:\n"
                             "Три шоколода\n"
                             "Тирамису\n"
                             "торт\n"
                             "Мороженое")
    elif message.text == 'напитки':
        await message.answer("Вы выбрали раздел 'напитки'. Вот наше меню напитков:\n"
                             "кола\n"
                             "пепси\n"
                             "фанта\n"
                             "спрайт"
                             "вода")