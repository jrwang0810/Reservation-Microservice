import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = "admin"
        pw = "E6156cloud"
        h = "thumbsup.cqbpyq6u5l7q.us-east-1.rds.amazonaws.com"
        print(usr, pw, h)
        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def TestConnection():

        sql = "SELECT * FROM Registration.registration";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result