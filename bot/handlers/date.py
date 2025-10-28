from aiogram import F, Router, types
import bot.keyboard_text as kbtext

router = Router()

@router.message(F.text == kbtext.find_date)
async def cmd_departure(message: types.Message):
    await message.answer("Скільки років зараз вашій дитині?")