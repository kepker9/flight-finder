from aiogram import F, Router, types
from aiogram.filters import Command
import bot.keyboard_text as kbtext

router = Router()

@router.message(F.text == kbtext.find_departure)
async def cmd_departure(message: types.Message):
    await message.answer("Скільки років зараз вашій дитині?")
