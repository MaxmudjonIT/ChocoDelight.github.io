from KeyBoards import language
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, SuccessfulPayment
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, F, types
from dotenv import load_dotenv
import os

load_dotenv()
PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def starting_bot(message: types.Message):
    await message.answer("Здравствуйте! Давайте для начала выберем язык обслуживания!\n\n"
                         "Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik.\n\n"
                         "Hi! Let's first we choose language of serving!\n\n", reply_markup=language)


@dp.message(Command())
async def echo(message: types.Message):
    await message.answer("Hello")
