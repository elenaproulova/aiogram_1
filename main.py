import asyncio, aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN, API_KEY
from googletrans import Translator
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
@dp.message(F.photo)
async def react_photo(message: Message):
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile("1718883178.ogg")
    await message.answer_voice(voice)



@dp.message(Command('weather'))
async def weather(message: Message):
    await message.answer(await get_weather())


@dp.message(Command('help'))
async def help(message: Message):
   await message.answer("Этот бот умеет выполнять команды:\n/start \n/help \n/weather")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}')

@dp.message()
async def handle_text(message: Message):
    original_text = message.text
    translator = Translator()
    try:
        # Переводим текст на английский
        translated = translator.translate(original_text, dest='en').text
        await message.answer(f"Перевод на английский:\n{translated}")
    except Exception as e:
        await message.answer("Произошла ошибка при переводе.")
        print(f"Ошибка перевода: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())