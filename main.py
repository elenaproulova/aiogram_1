import asyncio, aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def get_weather():
    city = "Yekaterinburg"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                weather_desc = data['weather'][0]['description'].capitalize()
                temp = data['main']['temp']

                return (
                    f"Погода в Екатеринбурге:\n"
                    f"{weather_desc}\n"
                    f"Температура: {temp}°C\n"
                )
            else:
                return "Не удалось получить данные о погоде."

@dp.message(Command('weather'))
async def weather(message: Message):
    weather_info = await get_weather()
    await message.answer(weather_info)


@dp.message(Command('weather'))
async def weather(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start \n/help \n/weather")

#@dp.message(Command('help'))
#async def help(message: Message):
#    await message.answer("Этот бот умеет выполнять команды:\n/start \n/help \n/weather")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я бот!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())