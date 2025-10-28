from aiogram import Router, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardRemove

import bot.keyboards as kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f'Hi! To start looking for tickets, type /find',
                         reply_markup=kb.start)

@router.message(Command("find"))
async def cmd_find(message: types.Message):
    await message.answer(f'Choose one of the following:',
                         reply_markup=kb.find)
