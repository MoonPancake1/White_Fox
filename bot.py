from aiogram.utils import executor
from create_bot import dp
from Handlers import cs_money_handler, other, settings, admin


other.register_handlers_other(dp)
settings.register_handlers_settings(dp)
cs_money_handler.register_handlers_cs_money_handler(dp)


# Главная функция main()
def main():
    executor.start_polling(dp)
    

# Если файл запускается не как модуль, то выполняется функция main()
if __name__ == '__main__':
    main()