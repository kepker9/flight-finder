from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = f'/find')]
], resize_keyboard=True)

find = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = f'Find the best departure airport')],
    [KeyboardButton(text = f'Find the best destination airport')],
    [KeyboardButton(text = f'Find the best date for the travel')]
], resize_keyboard=True)