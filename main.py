import asyncio, aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, API_KEY
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def get_weather():
    city = "Yekaterinburg"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp']
    return (
        f"Погода в Екатеринбурге:\n"
        f"Температура: {temp}°C\n"
    )

@dp.message(Command('weather'))
async def weather(message: Message):
    await message.answer(await get_weather())


@dp.message(Command('help'))
async def help(message: Message):
   await message.answer("Этот бот умеет выполнять команды:\n/start \n/help \n/weather")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я бот!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())