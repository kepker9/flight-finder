from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import bot.keyboard_text as kbtext

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = f'/find')]
], resize_keyboard=True)

find = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = kbtext.find_departure)],
    [KeyboardButton(text = kbtext.find_destination)],
    [KeyboardButton(text = kbtext.find_date)],
], resize_keyboard=True)