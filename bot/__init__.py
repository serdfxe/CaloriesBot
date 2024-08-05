from typing import Tuple
from aiogram import Bot, Dispatcher

from bot.modules.diary import diary_router
from bot.modules.start import start_router
from bot.modules.help import help_router

from config import OWNER_ID, TOKEN


def create_dp() -> Dispatcher:
    dp = Dispatcher()
    
    dp.include_routers(
        start_router,
        diary_router,
        help_router,
    )

    return dp

async def main():
    bot = Bot(token=TOKEN)

    await bot.send_message(OWNER_ID, "START!!!")

    dp = create_dp()

    await dp.start_polling(bot)
