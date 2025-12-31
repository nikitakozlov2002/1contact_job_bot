from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Оставить заявку')],
    [KeyboardButton(text='Помощь')]
    ], 
    resize_keyboard=True,
    input_field_placeholder = 'Скорее оставляйте заявку!')

after_start = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='О нас')]], resize_keyboard=True)

after_about = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Оставить заявку')]], resize_keyboard=True)

experience = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='До 1 года')],
    [KeyboardButton(text='От 1 до 3 лет')],
    [KeyboardButton(text='От 3 до 5 лет')],
    [KeyboardButton(text='От 5 до 10 лет')],
    [KeyboardButton(text='Более 10 лет')]
], 
resize_keyboard=True,
input_field_placeholder = 'Укажите Ваш опыт...')

yes_or_not = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Да')],
    [KeyboardButton(text='Нет')]
], 
resize_keyboard=True,
input_field_placeholder = 'Выберите один из предложенных вариантов')