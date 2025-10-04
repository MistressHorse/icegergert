import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config import config
from aiogram.filters import Command
import random
import traceback

try:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    with open("ICEGERGERT.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()


    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("Напиши /swaga, чтобы получить строчку из песен ICEGERGERT, характеризующую твой день")


    @dp.message(Command("swaga"))
    async def cmd_swaga(message: types.Message):
        line = random.choice(lines)
        await message.answer(line)


    async def main():
        await dp.start_polling(bot)
        print("Bot is activated...")


    if __name__ == "__main__":
        asyncio.run(main())
except Exception:
    print("Ошибка при запуске бота:")
    traceback.print_exc()
