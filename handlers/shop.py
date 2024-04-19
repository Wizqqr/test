from aiogram import Router, F, types
from aiogram.filters import Command
from bot import database


shop_router = Router()

@shop_router.message(Command('shop'))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Десерт'),
                types.KeyboardButton(text='Второе')
            ],
            [
                types.KeyboardButton(text='Закуска'),
                types.KeyboardButton(text='Суп')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Выберите вид блюд', reply_markup=kb)


kinds = ['десерт', 'второе', 'закуска', 'суп']


@shop_router.message(F.text.lower().in_(kinds))
async def show_food(message: types.Message):
    kind = message.text.lower()
    print(kind)
    kb = types.ReplyKeyboardRemove()
    data = await database.fetch(
        """
        SELECT food.* FROM food 
        JOIN kinds ON food.kind_id = kinds.id
        WHERE kinds.name = ?
        """,
        (kind,),
        fetch_type='all'
    )
    if not data:
        await message.answer('По вашему запросу ничего не найдено', reply_markup=kb)
    await message.answer(f'Все наши блюда категории {kind}:')
    for food in data:
        price = food['price']
        name = food['name']
        photo = types.FSInputFile(food['picture'])
        await message.answer_photo(
            photo=photo,
            caption=f'Названия блюда: {name}\nЦена: {price} сом'
        )