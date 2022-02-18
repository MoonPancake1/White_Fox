from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink, hunderline
from create_bot import dp, bot, BotDB


# Начало взаимодействия с телеграм ботом
# @dp.message_handler(commands='start')
async def start(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)
        BotDB.add_record(message.from_user.id, 75, 50, -10)
    start_buttons = ['Парсер цен 🛒', 'О проекте ⭐️']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    
    await message.answer('Выберите нужный пункт:', reply_markup=keyboard)
        
 
# Кнопка назад
# @dp.message_handler(Text(equals='В меню 🔙'))
async def back(message: types.Message):
    start_buttons = ['Парсер цен 🛒', 'О проекте ⭐️']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выберите нужный пункт:', reply_markup=keyboard)
    

# Информация о проекте
# @dp.message_handler(Text(equals='О проекте ⭐️'))
async def about(message: types.Message):
    name_program = '"White Fox Lab"'
    start_buttons = ['В меню 🔙']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    
    message_about_users =   f'{hbold("White Fox Lab - Telegram bot v1.5")} \n\n' \
        f'{hbold(f"Чернышев Владислав - CEO {name_program}")}\n\n' \
        f"{hbold('© 2021-2022 White Fox Lab - Все права защищены!')}"
    
    await message.answer(message_about_users, reply_markup=keyboard)


# Список доступных маркетплейсов и параметры
# @dp.message_handler(Text(equals='Парсер цен 🛒'))
async def Marketplace(message: types.Message):
    marketplace_buttons = ['Cs money 🐒', 'Параметры ⚙️', 'В меню 🔙']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*marketplace_buttons)
    
    await message.answer('Выберите нужный маркетплейс:', reply_markup=keyboard)
    
    
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(back, Text(equals='В меню 🔙'))
    dp.register_message_handler(about, Text(equals='О проекте ⭐️'))
    dp.register_message_handler(Marketplace, Text(equals='Парсер цен 🛒'))