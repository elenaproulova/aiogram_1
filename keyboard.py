from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет!"), KeyboardButton(text="Пока!")]
], resize_keyboard=True)



inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", callback_data='news', url='https://vkvideo.ru/video-40281195_456259098?ref_domain=yastatic.net')],
   [InlineKeyboardButton(text="Музыка", callback_data='music', url='https://vkvideo.ru/video-40281195_456259098?ref_domain=yastatic.net')],
   [InlineKeyboardButton(text="Видео", callback_data='video', url='https://vkvideo.ru/video-40281195_456259098?ref_domain=yastatic.net')]
])

# test = ["Опция 1", "Опция 2"]
#
# async def test_keyboard():
#    keyboard = InlineKeyboardBuilder()
#    for key in test:
#        keyboard.add(InlineKeyboardButton(text=key))
#        return keyboard.adjust(2).as_markup()

inline_keyboard_test_2 = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='more')],
])

test_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Опция 1", callback_data='option1')],
    [InlineKeyboardButton(text="Опция 2", callback_data='option2')],
])
