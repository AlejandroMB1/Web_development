import pymysql
from db_config import mysql

class UsersRepository(object):
    def __init__(self):
        self.conn = mysql.connect()

    def login(self, username, password):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id AS id FROM user WHERE username=%s AND password=%s", (username, password))
        row = cursor.fetchone()
        cursor.close()
        return row

    def get_user_by_id(self, id):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT email, name, username FROM user WHERE id=%s", id)
        row = cursor.fetchone()
        cursor.close()
        return row
    
    def get_user_by_name(self, name):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT email, name, username FROM user WHERE name=%s", name)
        row = cursor.fetchone()
        cursor.close()
        return row
    
    def get_all_users(self):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user")
        row = cursor.fetchall()
        cursor.close()
        return row

    def crear_nuevo_usuario(self, _email, _name, _password, _username):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO user(email, name, password, username) VALUES(%s,%s,%s,%s)",(_email, _name, _password, _username))
        #affectedRows = cursor.rowcount()
        row = cursor.fetchone()
        #affectedRows = row[0]
        cursor.close()
        print(row)
        self.conn.commit()
        return row