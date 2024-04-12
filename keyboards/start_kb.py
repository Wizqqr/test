from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='наш адрес', callback_data='address'),
         InlineKeyboardButton(text='наш сайт', url='https://www.vecteezy.com/free-photos')],
        [InlineKeyboardButton(text='наше меню', callback_data='menu'),
         InlineKeyboardButton(text='наш телефон', callback_data='phone')],
        [InlineKeyboardButton(text='Опросник', callback_data='service')]
    ])
    return kb