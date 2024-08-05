from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from messages_config import help_message


help_router = Router(name="help_router")


@help_router.message(Command("help"))
async def help_command_handler(message: Message):
    await message.answer(help_message)
