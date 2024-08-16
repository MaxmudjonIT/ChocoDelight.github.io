from aiogram import Bot, Dispatcher, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import os
from Bot.ChocoDelight_Code.DataBase import db_cursor, db_connect
from Bot.ChocoDelight_Code.StatusGroup import Registration
from Bot.ChocoDelight_Code.KeyBoards import Phone, language, Home

# Загрузка токенов из .env файла
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def starting_bot(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    db_cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = db_cursor.fetchone()

    if user:
        await start_home(message)
    else:
        await message.answer("Здравствуйте! Для начала давайте определимся с языком обслуживания.\n\n"
                             "Keling, avvaliga xizmat ko'rsatish tilini tanlab olaylik.\n\n"
                             "Hello! Let's start by selecting the language for assistance!\n\n",
                             reply_markup=language)


@dp.message(F.text == "🇷🇺 Русский")
async def russian_registration(message: types.Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer("Прежде чем мы начнем, пожалуйста, сначала зарегистрируйтесь,"
                         " чтобы я мог помочь вам в полной мере. Это займет всего пару минут!\n\n"
                         "Как вас зовут?")


@dp.message(Registration.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.phone)
    await message.answer("Спасибо! Теперь, пожалуйста, отправьте мне ваш номер телефона.", reply_markup=Phone)


@dp.message(Registration.phone, F.contact)
async def process_phone(message: types.Message, state: FSMContext):
    if message.contact:
        user_data = await state.get_data()
        user_name = user_data['name']
        user_phone = message.contact.phone_number
        user_id = message.from_user.id

        db_cursor.execute(
            "INSERT OR REPLACE INTO users (user_id, name, phone) VALUES (?, ?, ?)",
            (user_id, user_name, user_phone)
        )
        db_connect.commit()

        await state.clear()
        await message.answer(
            f"Спасибо, {user_name}! Вы успешно зарегистрированы с номером телефона: {user_phone}."
        )
        await start_home(message)
    else:
        await message.answer(
            "Пожалуйста, отправьте номер телефона, используя кнопку 'Отправить контакт'."
        )


@dp.message()
async def start_home(message: types.Message):
    await message.answer("Чтобы оформить заказ, нажмите на 🛍 Заказать.\n\n"
                         "Также вы можете ознакомиться с нашими акциями и найти ближайшие к вам филиалы.",
                         reply_markup=Home)
