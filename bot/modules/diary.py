from aiogram import Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command

from app.exceptions import IllegibilityException, TooLongDescriptionException
from app.services.calories_counter import CaloriesCounterService
from app.services.diary import DiaryService
from messages_config import CPFC_message, today_summary_message


diary_router = Router(name="calories_router")


@diary_router.callback_query(lambda call: call.data.startswith("cpfc_"))
async def cpfc_handler(callback: CallbackQuery):
    try:
        _, *cpfc = callback.data.split("_")

        cpfc = [int(i) for i in cpfc]

        DiaryService.record(callback.from_user.id, cpfc)
    except Exception as e:
        await callback.message.edit_text(callback.message.text + "\n\nЧто-то пошло не так ;(")

        raise e
    else:
        await callback.message.edit_text(callback.message.text + "\n\nЗаписал в дневник. Посмотреть: /diary", reply_markup=None)

@diary_router.message(Command("diary"))
async def diary_command_handler(message: Message):
    try:
        cpfc = DiaryService.get_today_summary(user_id=message.from_user.id)
    except Exception as e:
        await message.answer("Что-то пошло не так ;( Попробуйте позже.")

        raise e
    else:
        await message.answer(today_summary_message.format(calories=cpfc[0], protein=cpfc[1], fats=cpfc[2], carbs=cpfc[3]))

@diary_router.message()
async def dish_description_handler(message: Message):
    try:
        cpfc = CaloriesCounterService.count_cpfc(message.text)
    except IllegibilityException as e:
        await message.answer("Не получилось разобрать описание. Попробуйте ещё раз.")
    except TooLongDescriptionException as e:
        await message.answer("Слишком длинное описание. Попробуйте написать короче или разбить на несколько сообщений.")
    except Exception as e:
        await message.answer("Что-то пошло не так ;( Попробуйте позже.")

        raise e
    else:    
        buttons = [
            InlineKeyboardButton(text="Записать", callback_data="cpfc_" + "_".join([str(i) for i in cpfc]))
        ]

        keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons], row_width=1)

        await message.answer(CPFC_message.format(calories=cpfc[0], protein=cpfc[1], fats=cpfc[2], carbs=cpfc[3]), reply_markup=keyboard)
