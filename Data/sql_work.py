import sqlite3

class BotDB:
    
    def __init__(self, db_file):
        # Инициализация соединения с БД
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        
    
    def user_exists(self, user_id):
        # Проверяем, есть ли пользователь в БД
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))
    
    
    def get_user_id(self, user_id):
         # Получаем id пользователя по его user_id в телеграме
         result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
         return result.fetchone()[0]
     
     
    def add_user(self, user_id):
         # Добавляем пользователя в БД
         self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
         return self.conn.commit()
     
     
    def add_record(self, user_id, max_price, min_price, discount_percent):
        # Создаём запись о параметрах парсера
        self.cursor.execute("INSERT INTO `records` (`users_id`, `max_price`, `min_price`, `discount_percent`) VALUES(?, ?, ?, ?)",
            (user_id,
             max_price,
             min_price,
             discount_percent))
        return self.conn.commit()
    
    
    def delete_record(self, users_id):
        # Удаляем данные пользователя из базы данных
        self.cursor.execute("DELETE FROM `records` WHERE `users_id` = ?", (users_id,))
        return self.conn.commit()

    
    
    def get_user_settings(self, users_id):
        # Достаём значения из БД для пользователя
         max_price = self.cursor.execute("SELECT `max_price` FROM `records` WHERE `users_id` = ?", (users_id,)).fetchall()[0]
         min_price = self.cursor.execute("SELECT `min_price` FROM `records` WHERE `users_id` = ?", (users_id,)).fetchall()[0]
         discount_percent = self.cursor.execute("SELECT `discount_percent` FROM `records` WHERE `users_id` = ?", (users_id,)).fetchall()[0]
         return max_price, min_price, discount_percent
         
    
    def close(self):
        # Закрытие соединения с БД
        self.conn.close()