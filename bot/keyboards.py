from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import bot.keyboard_text as kbtext

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = f'/find')]
], resize_keyboard=True)

find = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = kbtext.find_departure)],
    [KeyboardButton(text = kbtext.find_destination)],
    [KeyboardButton(text = kbtext.find_date)]
], resize_keyboard=True)

departure_type = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = kbtext.departure_type_round_trip)],
    [KeyboardButton(text = kbtext.departure_type_one_way)]
], resize_keyboard=True)

destination_type = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = kbtext.destination_type_round_trip)],
    [KeyboardButton(text = kbtext.destination_type_one_way)]
], resize_keyboard=True)