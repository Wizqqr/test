from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def quality_service_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Excellent', callback_data='excellent'),
            InlineKeyboardButton(text='Good', callback_data='good')
        ],
        [
            InlineKeyboardButton(text='Normal', callback_data='normal'),
            InlineKeyboardButton(text='Bad', callback_data='bad')
        ]
    ])
    return kb


def service_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
          InlineKeyboardButton(text='Low', callback_data='low'),
          InlineKeyboardButton(text='High', callback_data='high')
        ],
        [
            InlineKeyboardButton(text='Medium', callback_data='medium')
        ]
    ])
    return kb
