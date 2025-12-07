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

