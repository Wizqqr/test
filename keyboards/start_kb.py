from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Опросник', callback_data='service')]
    ])
    return kb