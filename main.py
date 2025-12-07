import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv


load_dotenv()
logging.basicConfig(level=logging.INFO)


# bot and dispatcher
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ثبت نام دور ها"), KeyboardButton(text="ارتباط با اعضا")],
    ],
    resize_keyboard=True,
)


# intro/welcome message

WELCOME = (
    "سلام./n"
    "به ربات انجمن رباتیک و مکاترونیک دانشگاه نوشیروانی بابل خوش اومدی! /n"
    "از طریق ربات می تونی با اعضا در ارتباط باشی و همینطور در دوره ها و کلاس هامون شرکت کنی !/n" 
)

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(WELCOME, reply_markup= keyboard)
    