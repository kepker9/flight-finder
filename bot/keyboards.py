from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = f'/find')]
], resize_keyboard=True)

find = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = f'Обрати звідки летіти'), KeyboardButton(text = f'Обрати куди летіти'), KeyboardButton(text = f'Коли летіти')]
], resize_keyboard=True)