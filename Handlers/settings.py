import traceback

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink, hunderline
from Data.sql_work import BotDB
from Data.ErrorTypes import price_error
from create_bot import dp, bot, BotDB


# Параметры для парсинга
# # @dp.message_handler(Text(equals='Параметры ⚙️'))
async def settings_edits_menu(message: types.Message):
    users_id = message.from_user.id

    max_price, min_price, discount_percent = BotDB.get_user_settings(users_id)
    
    replace_symbol = ['(', ')', ',']
    
    max_price = str(max_price)
    min_price = str(min_price)
    discount_percent = str(discount_percent)
    
    for i in replace_symbol:
        for j in i:
            max_price = max_price.replace(j, '').strip()
            min_price = min_price.replace(j, '').strip()
            discount_percent = discount_percent.replace(j, '').strip()
            
    max_price = int(max_price)
    min_price = int(min_price)
    discount_percent = int(discount_percent)
    
        
    settings_message = f'⚙️ {hbold("Ваши текущие параметры парсинга: ")}\n\n' \
        f'Минимальная цена:  {hbold(min_price)}$\n' \
        f'Максимальная цена:  {hbold(max_price)}$\n' \
        f'Скидка:  от  {hbold(discount_percent)}% 💎'
        
    await message.answer(settings_message)
    
    settings_parse_buttons = ['Изменить 🔧', 'В меню 🔙']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*settings_parse_buttons)
    
    await message.answer('Изменить параметры?', reply_markup=keyboard)
    
    
# @dp.message_handler(Text(equals='Изменить 🔧'))
async def instractions(message: types.Message):
    await message.answer("⚙️ Введите команду /s и напишите значения по порядку: минимальная цена, максимальная цена, процент скидки", 
        reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Пример: /s  50  75  -10")
    

# @dp.message_handler(commands = ("settings", "s"), commands_prefix = "/!")
async def record(message: types.Message):
    cmd_variants = ('/settings', '/s', '!settings', '!s')
    
    value = message.text
    for i in cmd_variants:
        for j in i:
            value = value.replace(j, '').strip()
            
    value = value.split()
    users_id = message.from_user.id
    discount_percent = value.pop()
    max_price = value.pop()
    min_price = value.pop()
      
    try:
        if int(max_price) <= int(min_price) or int(discount_percent) > 0:
            raise price_error()    
        BotDB.delete_record(users_id)       
        BotDB.add_record(users_id, max_price, min_price, discount_percent) 
        
        settings_parse_buttons_exit = ['Изменить 🔧', 'В меню 🔙']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*settings_parse_buttons_exit)
        
        await message.answer("Параметры успешно сохранены! ✅", reply_markup=keyboard)
        
        settings_message_done = f'⚙️ {hbold("Ваши текущие параметры парсинга: ")}\n\n' \
            f'Минимальная цена:  {hbold(min_price)}$\n' \
            f'Максимальная цена:  {hbold(max_price)}$\n' \
            f'Скидка:  от  {hbold(discount_percent)}% 💎'
            
        await message.answer(settings_message_done)
        
        
    except Exception as _ex:
        await message.answer(f"Произошла ошибка! ❌")
        await message.answer(f"Повторите попытку и введите корректные значения.")
        print('Ошибка:\n', traceback.format_exc())
    
        settings_parse_buttons = ['Изменить 🔧', 'В меню 🔙']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*settings_parse_buttons)
        
        await message.answer('Изменить параметры?', reply_markup=keyboard)
        
        
def register_handlers_settings(dp: Dispatcher):
    dp.register_message_handler(settings_edits_menu, Text(equals='Параметры ⚙️')) # commands=['start'])
    dp.register_message_handler(instractions, Text(equals='Изменить 🔧'))
    dp.register_message_handler(record, commands=["settings", "s"])