from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from datetime import datetime
from bookservice.bookservice import BookService
from aiogram import types, F, Router
from bot import database


service_router = Router()


@service_router.callback_query(F.data == 'service')
async def start_service(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(BookService.name)
    await cb.message.answer('What is your name')


@service_router.message(BookService.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookService.age)
    await message.answer(f'Could you tell me your age?')



@service_router.message(BookService.age)
async def process_age(message: Message, state: FSMContext):
    age = int(message.text)
    if age < 7 or age > 60:
        await message.answer('You are too young or too old. Please try again.')
        await state.finish()
    elif age > 18:
        await state.update_data(age=age)
        await state.set_state(BookService.salary_or_grade)
        await message.answer('What is your salary?')
    else:
        await state.update_data(age=age)
        await state.set_state(BookService.occupation)
        await message.answer('What is your average grade in school?')


@service_router.message(BookService.salary_or_grade)
async def process_salary(message: Message, state: FSMContext):
    salary = int(message.text)
    await state.update_data(salary=salary)
    await state.set_state(BookService.occupation)
    await message.answer('What is your occupation?')


@service_router.message(BookService.salary_or_grade)
async def process_grade(message: Message, state: FSMContext):
    grade = float(message.text)
    await state.update_data(grade=grade)
    await state.set_state(BookService.occupation)
    await message.answer('What is your occupation?')


@service_router.message(BookService.occupation)
async def process_occupation(message: Message, state: FSMContext):
    occupation = message.text
    await state.update_data(occupation=occupation)
    data = await state.get_data()
    if 'salary' in data:
        await state.set_state(BookService.last)
    else:
        await state.set_state(BookService.last_Grade)
    await message.answer('Thank you! Your data has been processed.')

@service_router.message(BookService.last)
async def process_last_state(message: Message, state: FSMContext):
    await state.update_data(last=message.text)
    data = await state.get_data()
    print(data)
    await database.execute(
        'INSERT INTO service (name, age, occupation, salary_or_grade, last, last_Grade) VALUES (?, ?, ?, ?, ?, ?)',
        (data['name'], data['age'], data['occupation'], data['salary_or_grade'], data['last'], data['last_Grade'])
    )
    await message.answer(f"Name: {data['name']}\n"
                         f"Age: {data['age']}\n"
                         f"Occupation: {data['occupation']}\n"
                         f"Salary: {data['salary']}\n"
                         f"Last: {data['last']}")
    await state.finish()


@service_router.message(BookService.last_Grade)
async def process_last_grade_state(message: Message, state: FSMContext):
    await state.update_data(last_Grade=message.text)
    data = await state.get_data()
    print(data)
    await database.execute(
        'INSERT INTO service (name, age, occupation, salary_or_grade, last, last_Grade) VALUES (?, ?, ?, ?, ?, ?)',
        (data['name'], data['age'], data['occupation'], data['salary_or_grade'], data['last'], data['last_Grade'])
    )
    await message.answer(f"Name: {data['name']}\n"
                         f"Age: {data['age']}\n"
                         f"Occupation: {data['occupation']}\n"
                         f"Grade: {data['grade']}\n"
                         f"Last: {data['last']}")
    await state.finish()