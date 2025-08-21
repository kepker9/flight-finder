from aiogram import Router, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardRemove

import bot.keyboards as kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f'Вітаю! Щоб почати знаходити зі мною найкращі авіаквитки, напиши команду /find',
                         reply_markup=kb.start)

@router.message(Command("find"))
async def cmd_find(message: types.Message):
    await message.answer(f'Щоб знайти аеропорт <b>з якого</b> найвигідніше летіти, нажміть <u>Обрати звідки летіти</u>.\n\n'
                         f'Щоб знайти аеропорт <b>куди</b> найвигідніше летіти, нажміть <u>Обрати куди летіти</u>.\n\n'
                         f'Щоб взнати <b>в які дати</b> найвигідніше летіти, нажміть <u>Коли летіти</u>.',
                         parse_mode=ParseMode.HTML,
                         reply_markup=kb.find)
