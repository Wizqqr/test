from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()