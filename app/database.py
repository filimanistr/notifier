import sqlite3

class Database:
    def __init__(self):
        '''Подключаем БД'''
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()

    def add_user(self, user):
        self.c.execute("INSERT INTO users {} VALUES {}".format((tuple(user.keys(), )), tuple(user.values())))
        self.conn.commit()

    def get_user(self, user):
        self.c.execute("SELECT * FROM users WHERE id = ?", (user['id'], ))
        data = self.c.fetchone()
        if data != None:
            cursor = self.c.execute('select * from users')
            column_names = [description[0] for description in cursor.description]
            output = dict()
            for i in range(len(column_names)):
                output[column_names[i]] = data[i]
            return output
        return None

    def get_users(self):
        users = list()
        self.c.execute("SELECT id FROM users")
        data = self.c.fetchall()
        return data

    def close(self):
        self.c.close()
        self.conn.close()

