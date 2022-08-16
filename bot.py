import requests
import datetime
from config import BOT_TOKEN
from config import OW_TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from weather import get_weather

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=["start"])
async def start_command(message: types.message):
    await message.reply("Hi! Enter any city. I send you its weather")
@dp.message_handler()
async def get_message(message: types.message):
    msg = message.text
    try:
        answer = get_weather(msg, OW_TOKEN)
        await message.reply(answer)
    except:
        await message.reply("\U00002620 Check city's name \U00002620")

if __name__ == '__main__':
    executor.start_polling(dp)