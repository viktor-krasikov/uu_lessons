import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = os.getenv("TESTING_BOT")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"])
async def start(message):
    print("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_messages(message):
    print("Введите команду /start, чтобы начать общение.")


executor.start_polling(dp, skip_updates=True)
