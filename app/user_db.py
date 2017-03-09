# -*- coding: utf-8 -*-
import MySQLdb as mysql
import MySQLdb.cursors

HOST = 'localhost'
USER = 'root'
PASSWORD = 'balbin'
DATABASE = 'web_prg'

class User:
    def __init__(self):
        self.db = mysql.connect(HOST, USER, PASSWORD, DATABASE,
          use_unicode=True, charset="utf8", cursorclass=MySQLdb.cursors.DictCursor)

        self.cursor = self.db.cursor()

    def register(self, name, password):
        query = """INSERT INTO user (username, password)
                    VALUES (%s, %s)"""

        # READ MORE:
        # SQL Injection
        self.cursor.execute(query, (name, password))
        self.db.commit()
        self.db.close()

    def check_user(self, name, password):
        query = """SELECT * from user
            where username = %s and password = %s"""

        self.cursor.execute(query, (name, password))
        self.db.close()

        return self.cursor.fetchone()

    def get_all_users(self):
        query = """SELECT * from user"""

        self.cursor.execute(query)
        self.db.close()

        return self.cursor.fetchall()







