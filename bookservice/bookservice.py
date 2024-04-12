from aiogram.fsm.state import State, StatesGroup


class BookService(StatesGroup):
    name = State()
    number = State()
    data = State()
    quality = State()
    cleanable = State()