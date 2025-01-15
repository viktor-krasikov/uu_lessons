import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("TESTING_BOT")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text="Рассчитать"))
kb.add(KeyboardButton(text="Информация"))

ikb = InlineKeyboardMarkup(resize_keyboard=True)
ikb.add(InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"))
ikb.add(InlineKeyboardButton(text="Формулы расчёта'", callback_data="formulas"))


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text=["Рассчитать"])
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=ikb)


@dp.callback_query_handler(text=["calories"])
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await UserState.age.set()


@dp.callback_query_handler(text=["formulas"])
async def formulas(call):
    await call.message.answer("Формула Миффлина-Сан Жеора:\n"
                              "для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n"
                              "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    try:
        await state.update_data(age=float(message.text))
    except Exception as e:
        await message.answer('Возраст должен быть числом. Введите заново:')
        return
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    try:
        await state.update_data(growth=float(message.text))
    except Exception as e:
        await message.answer('Рост должен быть числом. Введите заново:')
        return
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    try:
        await state.update_data(weight=float(message.text))
    except Exception as e:
        await message.answer('Вес должен быть числом. Введите заново:')
        return
    data = await state.get_data()
    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
    await message.answer(f'Ваша норма калорий: {calories} ккал.')
    await state.finish()


executor.start_polling(dp, skip_updates=True)
