import json
import time
import traceback

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink, hunderline
from Data.parse_cs_money import collect_data
from create_bot import dp, bot, BotDB


# Маркетплейс "cs.money" и все доступные для него функции парсера
# @dp.message_handler(Text(equals='Cs money 🐒'))
async def cs_money(message: types.Message):
    cs_money_buttons = ['Ножи🔪', 'СВ🌹', 'Пистолеты🔫', 'ПП🐧', 'ШВ🐉', 'Все предметы❤️', 'В меню 🔙']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*cs_money_buttons)
    
    await message.answer('Выберите нужный пункт:', reply_markup=keyboard)
    
 
# Парсер категории: Ножи
# @dp.message_handler(Text(equals='Ножи🔪'))
async def get_discount_knife(message: types.Message):
    users_id = message.from_user.id
    
    try:
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
        
            
        settings_message = f'⚙️ {hbold("Параметры парсинга: ")}\n\n' \
            f'Категория парсинга: {hbold("Ножи 🔪")} \n' \
            f'Минимальная цена:  {hbold(min_price)}$\n' \
            f'Максимальная цена:  {hbold(max_price)}$\n' \
            f'Скидка:  от  {hbold(discount_percent)}% 💎'
                
        await message.answer(settings_message)
        await message.answer('Ожидайте...')
        
        collect_data(
                    cat_type = '&type=2', 
                    max_price = max_price, 
                    min_price = min_price, 
                    discount_procent = int(discount_percent),
                    users_id = users_id
                    ) # Парсинг ножей
            
        with open(f'Data/Result_and_setup/result{users_id}.json', encoding='utf-8') as file:
            data = json.load(file)
            
        if len(data) > 0:
            for index, item in enumerate(data):
                card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
                    f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
                    f'{hbold("Цена: ")}{item.get("item_price")}$ 🔥'
                        
                        
                if index%20 == 0:
                    time.sleep(5)
                        
                await message.answer(card)
            await message.answer(f'Всего нашлось: {hbold(len(data))} предмета(ов) ✅')
                
        elif len(data) == 0:
            await message.answer(f'К сожалению, по вашему запросу ничего не нашлось ❌')
            
    except TypeError:
        await message.answer('К сожалению, по вашему запросу ничего не нашлось ❌')
        
    except:
        await message.answer('Произошла ошибка! ⚙️')
        await message.answer('Попробуйте указать диапозон цен чуть меньше, либо повторите попытку 🧐')
        print('Ошибка:\n', traceback.format_exc())


# Парсер категории: Снайперские винтовки
# @dp.message_handler(Text(equals='СВ🌹'))
async def get_discount_sv(message: types.Message):
    users_id = message.from_user.id
    
    try:
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
        
            
        settings_message = f'⚙️ {hbold("Параметры парсинга: ")}\n\n' \
            f'Категория парсинга: {hbold("Снайперские винтовки 🌹")} \n' \
            f'Минимальная цена:  {hbold(min_price)}$\n' \
            f'Максимальная цена:  {hbold(max_price)}$\n' \
            f'Скидка:  от  {hbold(discount_percent)}% 💎'
                
        await message.answer(settings_message)
        await message.answer('Ожидайте...')
        
        collect_data(
                    cat_type = '&type=4', 
                    max_price = max_price, 
                    min_price = min_price, 
                    discount_procent = int(discount_percent),
                    users_id = users_id
                    ) # Парсинг снайперских винтовок
            
        with open(f'Data/Result_and_setup/result{users_id}.json', encoding='utf-8') as file:
            data = json.load(file)
            
        if len(data) > 0:
            for index, item in enumerate(data):
                card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
                    f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
                    f'{hbold("Цена: ")}{item.get("item_price")}$ 🔥'
                        
                        
                if index%20 == 0:
                    time.sleep(5)
                        
                await message.answer(card)
            await message.answer(f'Всего нашлось: {hbold(len(data))} предмета(ов) ✅')
                
        elif len(data) == 0:
            await message.answer(f'К сожалению, по вашему запросу ничего не нашлось ❌')
            
    except TypeError:
        await message.answer('К сожалению, по вашему запросу ничего не нашлось ❌')
        
    except:
        await message.answer('Произошла ошибка! ⚙️')
        await message.answer('Попробуйте указать диапозон цен чуть меньше, либо повторите попытку 🧐')
        print('Ошибка:\n', traceback.format_exc())
        

# Парсер категории: Пистолеты
# @dp.message_handler(Text(equals='Пистолеты🔫'))
async def get_discount_pistol(message: types.Message):
    users_id = message.from_user.id
    
    try:
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
        
            
        settings_message = f'⚙️ {hbold("Параметры парсинга: ")}\n\n' \
            f'Категория парсинга: {hbold("Пистолеты🔫")} \n' \
            f'Минимальная цена:  {hbold(min_price)}$\n' \
            f'Максимальная цена:  {hbold(max_price)}$\n' \
            f'Скидка:  от  {hbold(discount_percent)}% 💎'
                
        await message.answer(settings_message)
        await message.answer('Ожидайте...')
        
        collect_data(
                    cat_type = '&type=5', 
                    max_price = max_price, 
                    min_price = min_price, 
                    discount_procent = int(discount_percent),
                    users_id = users_id
                    ) # Парсинг пистолетов
            
        with open(f'Data/Result_and_setup/result{users_id}.json', encoding='utf-8') as file:
            data = json.load(file)
            
        if len(data) > 0:
            for index, item in enumerate(data):
                card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
                    f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
                    f'{hbold("Цена: ")}{item.get("item_price")}$ 🔥'
                        
                        
                if index%20 == 0:
                    time.sleep(5)
                        
                await message.answer(card)
            await message.answer(f'Всего нашлось: {hbold(len(data))} предмета(ов) ✅')
                
        elif len(data) == 0:
            await message.answer(f'К сожалению, по вашему запросу ничего не нашлось ❌')
            
    except TypeError:
        await message.answer('К сожалению, по вашему запросу ничего не нашлось ❌')
        
    except:
        await message.answer('Произошла ошибка! ⚙️')
        await message.answer('Попробуйте указать диапозон цен чуть меньше, либо повторите попытку 🧐')
        print('Ошибка:\n', traceback.format_exc())
        

# Парсер категории: Пистолеты-пулемёты
# @dp.message_handler(Text(equals='ПП🐧'))
async def get_discount_PP(message: types.Message):
    users_id = message.from_user.id
    
    try:
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
        
            
        settings_message = f'⚙️ {hbold("Параметры парсинга: ")}\n\n' \
            f'Категория парсинга: {hbold("Пистолеты-пулемёты 🐧")} \n' \
            f'Минимальная цена:  {hbold(min_price)}$\n' \
            f'Максимальная цена:  {hbold(max_price)}$\n' \
            f'Скидка:  от  {hbold(discount_percent)}% 💎'
                
        await message.answer(settings_message)
        await message.answer('Ожидайте...')
        
        collect_data(
                    cat_type = '&type=6', 
                    max_price = max_price, 
                    min_price = min_price, 
                    discount_procent = int(discount_percent),
                    users_id = users_id
                    ) # Парсинг пистолетов-пулемётов
            
        with open(f'Data/Result_and_setup/result{users_id}.json', encoding='utf-8') as file:
            data = json.load(file)
            
        if len(data) > 0:
            for index, item in enumerate(data):
                card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
                    f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
                    f'{hbold("Цена: ")}{item.get("item_price")}$ 🔥'
                        
                        
                if index%20 == 0:
                    time.sleep(5)
                        
                await message.answer(card)
            await message.answer(f'Всего нашлось: {hbold(len(data))} предмета(ов) ✅')
                
        elif len(data) == 0:
            await message.answer(f'К сожалению, по вашему запросу ничего не нашлось ❌')
            
    except TypeError:
        await message.answer('К сожалению, по вашему запросу ничего не нашлось ❌')
        
    except:
        await message.answer('Произошла ошибка! ⚙️')
        await message.answer('Попробуйте указать диапозон цен чуть меньше, либо повторите попытку 🧐')
        print('Ошибка:\n', traceback.format_exc())


# Парсер категории: Штурмовые винтовки
# @dp.message_handler(Text(equals='ШВ🐉'))
async def get_discount_shv(message: types.Message):
    users_id = message.from_user.id
    
    try:
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
        
            
        settings_message = f'⚙️ {hbold("Параметры парсинга: ")}\n\n' \
            f'Категория парсинга: {hbold("Штурмовые винтовки 🐉")} \n' \
            f'Минимальная цена:  {hbold(min_price)}$\n' \
            f'Максимальная цена:  {hbold(max_price)}$\n' \
            f'Скидка:  от  {hbold(discount_percent)}% 💎'
                
        await message.answer(settings_message)
        await message.answer('Ожидайте...')
        
        collect_data(
                    cat_type = '&type=3', 
                    max_price = max_price, 
                    min_price = min_price, 
                    discount_procent = int(discount_percent),
                    users_id = users_id
                    ) # Парсинг штурмовых винтовок
            
        with open(f'Data/Result_and_setup/result{users_id}.json', encoding='utf-8') as file:
            data = json.load(file)
            
        if len(data) > 0:
            for index, item in enumerate(data):
                card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
                    f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
                    f'{hbold("Цена: ")}{item.get("item_price")}$ 🔥'
                        
                        
                if index%20 == 0:
                    time.sleep(5)
                        
                await message.answer(card)
            await message.answer(f'Всего нашлось: {hbold(len(data))} предмета(ов) ✅')
                
        elif len(data) == 0:
            await message.answer(f'К сожалению, по вашему запросу ничего не нашлось ❌')
            
    except TypeError:
        await message.answer('К сожалению, по вашему запросу ничего не нашлось ❌')
        
    except:
        await message.answer('Произошла ошибка! ⚙️')
        await message.answer('Попробуйте указать диапозон цен чуть меньше, либо повторите попытку 🧐')
        print('Ошибка:\n', traceback.format_exc())
    

# Парсер категории: Без категории
# @dp.message_handler(Text(equals='Все предметы❤️'))
async def get_discount_all(message: types.Message):
    users_id = message.from_user.id
    
    try:
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
        
            
        settings_message = f'⚙️ {hbold("Параметры парсинга: ")}\n\n' \
            f'Категория парсинга: {hbold("Все предметы❤️")} \n' \
            f'Минимальная цена:  {hbold(min_price)}$\n' \
            f'Максимальная цена:  {hbold(max_price)}$\n' \
            f'Скидка:  от  {hbold(discount_percent)}% 💎'
                
        await message.answer(settings_message)
        await message.answer('Ожидайте...')
        
        collect_data(
                    cat_type = '', 
                    max_price = max_price, 
                    min_price = min_price, 
                    discount_procent = int(discount_percent),
                    users_id = users_id
                    ) # Парсинг всех предметов
            
        with open(f'Data/Result_and_setup/result{users_id}.json', encoding='utf-8') as file:
            data = json.load(file)
            
        if len(data) > 0:
            for index, item in enumerate(data):
                card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
                    f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
                    f'{hbold("Цена: ")}{item.get("item_price")}$ 🔥'
                        
                        
                if index%20 == 0:
                    time.sleep(5)
                        
                await message.answer(card)
            await message.answer(f'Всего нашлось: {hbold(len(data))} предмета(ов) ✅')
                
        elif len(data) == 0:
            await message.answer(f'К сожалению, по вашему запросу ничего не нашлось ❌')
            
    except TypeError:
        await message.answer('К сожалению, по вашему запросу ничего не нашлось ❌')
        
    except:
        await message.answer('Произошла ошибка! ⚙️')
        await message.answer('Попробуйте указать диапозон цен чуть меньше, либо повторите попытку 🧐')
        print('Ошибка:\n', traceback.format_exc())
        
        
def register_handlers_cs_money_handler(dp: Dispatcher):
    dp.register_message_handler(cs_money, Text(equals='Cs money 🐒'))
    dp.register_message_handler(get_discount_knife, Text(equals='Ножи🔪'))
    dp.register_message_handler(get_discount_sv, Text(equals='СВ🌹'))
    dp.register_message_handler(get_discount_pistol, Text(equals='Пистолеты🔫'))
    dp.register_message_handler(get_discount_PP, Text(equals='ПП🐧'))
    dp.register_message_handler(get_discount_shv, Text(equals='ШВ🐉'))
    dp.register_message_handler(get_discount_all, Text(equals='Все предметы❤️'))
