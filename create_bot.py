from aiogram import Bot, Dispatcher, executor, types
from Data.sql_work import BotDB
from Data.config import TOKEN

bot = Bot(token = TOKEN, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot)
BotDB = BotDB('Data/Result_and_setup/data_base_users.db')