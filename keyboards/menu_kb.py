from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu_kb():
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='первые блюда'),
         KeyboardButton(text='вторые блюда')],
        [KeyboardButton(text='десерт'),
         KeyboardButton(text='напитки')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True)
    return kb

