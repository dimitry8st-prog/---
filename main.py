import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# Загружаем настройки
load_dotenv()

# Настраиваем логи
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Берем токен бота
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    print("ОШИБКА: Создай файл .env с BOT_TOKEN=твой_токен")
    exit()

# Создаем бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("🎉 Бот работает! Напиши мне что-нибудь!")

# Обработчик всех сообщений
@dp.message()
async def echo_all(message: Message):
    text = message.text
    await message.answer(f"Эхо: {text}")

# Запуск бота
async def main():
    print("🚀 Запускаю бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())