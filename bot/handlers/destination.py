from aiogram import F, Router, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from datetime import datetime
from aiogram.types import ReplyKeyboardRemove

from bot.helper_functions import parse_names
import bot.keyboard_text as kbtext
import bot.keyboards as kb
from functions.best_airport_to_fly import best_airport_to_fly_to, best_airport_to_fly_to_rt

router = Router()

# -----------------------
# ONE-WAY DESTINATION FLOW
# -----------------------
class OneWayDestination(StatesGroup):
    departure_city = State()
    destination_cities = State()
    date = State()


@router.message(F.text == kbtext.find_destination)
async def cmd_destination(message: types.Message):
    await message.answer(
        "Do you need a round-trip or one-way ticket?",
        reply_markup=kb.destination_type
    )


@router.message(F.text == kbtext.destination_type_one_way)
async def cmd_destination_ow(message: types.Message, state: FSMContext):
    await message.answer(
        "Type the airport/city you will fly from",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(OneWayDestination.departure_city)


@router.message(OneWayDestination.departure_city)
async def ow_departure_city(message: types.Message, state: FSMContext):
    await state.update_data(departure=message.text)
    await message.answer("List all of the airports/cities you consider flying to")
    await state.set_state(OneWayDestination.destination_cities)


@router.message(OneWayDestination.destination_cities)
async def ow_destination_cities(message: types.Message, state: FSMContext):
    await state.update_data(destinations=message.text)
    await message.answer("Type the date of your flight in format yyyy-mm-dd")
    await state.set_state(OneWayDestination.date)


@router.message(OneWayDestination.date)
async def ow_date(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text)
    user_data = await state.get_data()

    airport_from = user_data["departure"]
    destinations = parse_names(user_data["destinations"])
    date = datetime.strptime(user_data["date"], "%Y-%m-%d").date()

    ans = best_airport_to_fly_to(airport_from, destinations, date)
    await message.answer(ans)
    await state.clear()


# -----------------------
# ROUND-TRIP DESTINATION FLOW
# -----------------------
class RoundTripDestination(StatesGroup):
    departure_city = State()
    destination_cities = State()
    start_date = State()
    end_date = State()


@router.message(F.text == kbtext.destination_type_round_trip)
async def cmd_destination_rt(message: types.Message, state: FSMContext):
    await message.answer(
        "Type the airport/city you will fly from",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(RoundTripDestination.departure_city)


@router.message(RoundTripDestination.departure_city)
async def rt_departure_city(message: types.Message, state: FSMContext):
    await state.update_data(departure=message.text)
    await message.answer("List all of the airports/cities you consider flying to")
    await state.set_state(RoundTripDestination.destination_cities)


@router.message(RoundTripDestination.destination_cities)
async def rt_destination_cities(message: types.Message, state: FSMContext):
    await state.update_data(destinations=message.text)
    await message.answer("Type the start date of your trip (yyyy-mm-dd)")
    await state.set_state(RoundTripDestination.start_date)


@router.message(RoundTripDestination.start_date)
async def rt_start_date(message: types.Message, state: FSMContext):
    await state.update_data(start_date=message.text)
    await message.answer("Type the return date of your trip (yyyy-mm-dd)")
    await state.set_state(RoundTripDestination.end_date)


@router.message(RoundTripDestination.end_date)
async def rt_end_date(message: types.Message, state: FSMContext):
    await state.update_data(end_date=message.text)
    user_data = await state.get_data()

    airport_from = user_data["departure"]
    destinations = parse_names(user_data["destinations"])
    start_date = datetime.strptime(user_data["start_date"], "%Y-%m-%d").date()
    end_date = datetime.strptime(user_data["end_date"], "%Y-%m-%d").date()

    ans = best_airport_to_fly_to_rt(airport_from, destinations, start_date, end_date)
    await message.answer(ans)
    await state.clear()
