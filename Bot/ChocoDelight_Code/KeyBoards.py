from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

language = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇺🇸 English")]
], resize_keyboard=True)

Phone = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отправить номер телефона 📲", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

Home = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🛍 Заказать")],
    [KeyboardButton(text="✍️ Оставить отзыв"), KeyboardButton(text="📋 Мои заказы")],
    [KeyboardButton(text="🏘 Филиалы"), KeyboardButton(text="ℹ️ О нас")],
    [KeyboardButton(text="⚙️ Настройки")]
], resize_keyboard=True)

