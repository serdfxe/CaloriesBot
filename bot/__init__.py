from aiogram import Bot, Dispatcher

from bot.modules.diary import diary_router
from bot.modules.start import start_router

from config import TOKEN


async def main():
    bot = Bot(token=TOKEN)

    dp = Dispatcher()
    
    dp.include_routers(
        start_router,
        diary_router,
    )

    await dp.start_polling(bot)
