from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет!"), KeyboardButton(text="Пока!")]
], resize_keyboard=True)



inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", callback_data='news', url='https://vkvideo.ru/video-40281195_456259098?ref_domain=yastatic.net')],
   [InlineKeyboardButton(text="Музыка", callback_data='music', url='https://vkvideo.ru/video-40281195_456259098?ref_domain=yastatic.net')],
   [InlineKeyboardButton(text="Видео", callback_data='video', url='https://vkvideo.ru/video-40281195_456259098?ref_domain=yastatic.net')]
])
