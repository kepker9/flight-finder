import asyncio
import logging
from aiogram import Bot, Dispatcher

from bot.config_reader import config
from bot.handlers import common, departure, destination, date

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher()


async def main():
    dp.include_routers(common.router, departure.router, destination.router, date.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

