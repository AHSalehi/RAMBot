import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

PROXY_URL = os.getenv("PROXY_URL")  # e.g. socks5h://127.0.0.1:1080

dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ثبت نام دوره‌ها"), KeyboardButton(text="ارتباط با اعضا")],
    ],
    resize_keyboard=True,
)

WELCOME = (
    "سلام.\n"
    "به ربات انجمن رباتیک و مکاترونیک دانشگاه نوشیروانی بابل خوش اومدی!\n"
    "از طریق ربات می‌تونی با اعضا در ارتباط باشی و همینطور در دوره‌ها و کلاس‌هامون شرکت کنی!"
)


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(WELCOME, reply_markup=keyboard)


async def main():
    session = AiohttpSession(proxy=PROXY_URL)
    bot = Bot(token=os.getenv("BOT_TOKEN"), session=session)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
