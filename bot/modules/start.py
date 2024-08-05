from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from app.services.register import RegisterService
from app.services.register.schemas import RegisterUserSchema
from bot.filters.registered import Registered


start_router = Router(name="start_router")


@start_router.message(~Registered())
async def not_registered_start_message_handler(message: Message):
    try:
        RegisterService.register_user(RegisterUserSchema.model_validate(message.from_user))
    except Exception as e:
        await message.answer("Произошла ошибка. Попробуйте позже. /start")

        raise e
    else:
        await message.answer("Добро пожаловать! Напиши подробное описание блюда, а я посчитаю его КБЖУ.")

@start_router.message(Command("start"), Registered())
async def registered_start_message_handler(message: Message):
    await message.answer("Приветствую! Напиши подробное описание блюда, а я посчитаю его КБЖУ.")

