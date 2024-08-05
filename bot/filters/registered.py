from aiogram.filters import Filter
from aiogram.types import Message

from app.services.register import RegisterService

class Registered(Filter):
    async def __call__(self, message: Message) -> bool:
        return RegisterService.registered(message.from_user.id)
