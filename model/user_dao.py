import json
import pymysql

class UserDao:

    def __init__(self, database):
        self.db = database

    def insert_user(self, user):
        cursor = self.db.cursor()
        sql = """
                insert into seller_keys(
                user
                ) values (
                %s
                )
                """
        cursor.execute(sql, (user['user']))
        self.db.commit()
        self.db.close()