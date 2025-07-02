import asyncio, aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN, API_KEY
# from googletrans import Translator
import requests
import keyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.text == "Привет!")
async def hello_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}')

@dp.message(F.text == "Пока!")
async def buy_button(message: Message):
   await message.answer(f'До свидания, {message.from_user.first_name}')

@dp.message(Command('links'))
async def link(message: Message):
   await message.answer(f'Ссылки на контент', reply_markup=kb.inline_keyboard_test)

@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
    await callback.answer("Новости подгружаются", show_alert=True)
    await callback.message.answer('Новости по ссылке')

@dp.callback_query(F.data == 'music')
async def music(callback: CallbackQuery):
    await callback.message.answer('Музыка по ссылке')

@dp.callback_query(F.data == 'video')
async def video(callback: CallbackQuery):
   await callback.message.answer('Видео по ссылке')

@dp.message(Command('dynamic'))
async def dynamic(message: Message):
   await message.answer(f'Ссылки на контент', reply_markup=kb.inline_keyboard_test_2)

@dp.callback_query(F.data == 'more')
async def news(callback: CallbackQuery):
    await callback.message.edit_text('Показать больше:', reply_markup=kb.test_keyboard())

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
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.main)

# @dp.message()
# async def handle_text(message: Message):
#     original_text = message.text
#     translator = Translator()
#     try:
#         # Переводим текст на английский
#         translated = translator.translate(original_text, dest='en').text
#         await message.answer(f"Перевод на английский:\n{translated}")
#     except Exception as e:
#         await message.answer("Произошла ошибка при переводе.")
#         print(f"Ошибка перевода: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())