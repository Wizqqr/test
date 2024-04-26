from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram import Bot, Dispatcher, types
from pathlib import Path
from db.database import Database


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()
dp = Dispatcher()
database = Database(
    Path(__file__).parent / 'db.sqlite'
)


async def set_my_menu():
    await bot.set_my_commands([
        types.BotCommand(command='start', description="всякое")
    ])