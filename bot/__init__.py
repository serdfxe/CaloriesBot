from aiogram import Bot, Dispatcher

from bot.modules.diary import diary_router
from bot.modules.start import start_router

from config import OWNER_ID, TOKEN


async def main():
    bot = Bot(token=TOKEN)

    dp = Dispatcher()
    
    dp.include_routers(
        start_router,
        diary_router,
    )

    await bot.send_message(OWNER_ID, "START!!!")

    await dp.start_polling(bot)
