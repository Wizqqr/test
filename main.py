import asyncio
import logging
from bot import dp, bot
from handlers.start import start_router
from handlers.callback import callback_router
from handlers.menu import menu_router
from handlers.service import service_router


async def main():
    dp.include_router(start_router)
    dp.include_router(callback_router)
    dp.include_router(menu_router)
    dp.include_router(service_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())