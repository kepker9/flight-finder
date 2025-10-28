from aiogram import F, Router, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from datetime import datetime

from aiogram.types import ReplyKeyboardRemove
from bot.helper_functions import parse_names

import bot.keyboard_text as kbtext
import bot.keyboards as kb
from functions.best_airport_to_fly import best_airport_to_fly_from

router = Router()

class OneWay(StatesGroup):
    departure_cities = State()
    destination_city = State()
    date = State()


@router.message(F.text == kbtext.find_departure)
async def cmd_departure(message: types.Message):
    await message.answer(f'Do you need a round-trip or one-way ticket?', reply_markup=kb.departure_type)


@router.message(F.text == kbtext.departure_type_one_way)
async def cmd_departure_ow(message: types.Message, state: FSMContext):
    await message.answer("List all of the airports/cities you consider flying from", reply_markup=ReplyKeyboardRemove())
    await state.set_state(OneWay.departure_cities)


@router.message(OneWay.departure_cities)
async def ow_departure_cities(message: types.Message, state: FSMContext):
    await state.update_data(departure=message.text)

    await message.answer("Type the airport you wish to fly")
    await state.set_state(OneWay.destination_city)


@router.message(OneWay.destination_city)
async def ow_destination_city(message: types.Message, state: FSMContext):
    await state.update_data(destination=message.text)

    await message.answer("Type the date of your flight in format yyyy-mm-dd")
    await state.set_state(OneWay.date)

#calling the actual method
@router.message(OneWay.date)
async def ow_date(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text)
    user_data = await state.get_data()

    departure = parse_names(user_data["departure"])
    destination = user_data["destination"]
    date = datetime.strptime(user_data["date"], "%Y-%m-%d").date()

    ans = best_airport_to_fly_from(departure, destination, date)

    await message.answer(
        ans
    )

    await state.clear()

#exactly the same shit for roundtrip now

