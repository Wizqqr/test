from aiogram.fsm.state import State, StatesGroup


class BookService(StatesGroup):
    name = State()
    age = State()
    occupation = State()
    salary_or_grade = State()
    last = State()
    last_Grade = State()