import asyncio, aiohttp
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN
import requests



bot = Bot(token=TOKEN)
dp = Dispatcher()

# def get_city():
#     url = 'https://kladr-api.ru/api.php'
#     response = requests.get(url)
#     data = response.json()
#
#
# def get_okato():

# Функция для получения кода ОКАТО по названию города
async def get_okato(city_name):
    url = 'https://kladr-api.ru/api.php'
    params = {
        'contentType': 'city',
        'q': city_name,
        'limit': 1,
        'apiKey': ''  # Можно оставить пустым, если API не требует ключ
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            if resp.status == 200:
                data = await resp.json()
                if data and 'result' in data and data['result']:
                    city = data['result'][0]
                    okato = city.get('okato', 'Код ОКАТО не найден')
                    name = city.get('name', 'Неизвестно')
                    return f"Город: {name}\nКод ОКАТО: {okato}"
                else:
                    return "Город не найден или нет данных."
            else:
                return "Ошибка при обращении к API."

# @dp.message(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Введите название города, чтобы получить код ОКАТО:")


@dp.message(Command("start"))
async def start_command(message: Message):
   await message.answer("Привет! Напиши мне название города, и я пришлю тебе его ОКАТО.")


@dp.message()
async def handle_city(message: types.Message):
    city_name = message.text.strip()
    response = await get_okato(city_name)
    await message.reply(response)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())