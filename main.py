import asyncio
from aiogram import Bot, types
from aiogram.filters import Command
import logging
from bot import dp,bot, set_my_menu, database
from handlers.start import start_router
from handlers.service import service_router
from handlers.echo import echo_router


async def on_startup(bot: Bot):
    await database.create_tables()
async def main():
    await set_my_menu()
    dp.include_router(start_router)
    dp.include_router(service_router)
    dp.include_router(echo_router)
    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
