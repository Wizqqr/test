from aiogram.fsm.state import State, StatesGroup


class BookService(StatesGroup):
    name = State()
    number = State()
    date = State()
    quality = State()
    cleanable = State()
    last = State()