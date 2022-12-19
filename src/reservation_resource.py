import pymysql

import os


class ReservationResource:

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
    def get_all_reservation():

        sql = "SELECT * FROM Reservation.reservation"
        conn = ReservationResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_reservation_by_email(email):

        sql = "SELECT * FROM Reservation.reservation WHERE email = {}".format(email)
        conn = ReservationResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()
        return result

    @staticmethod
    def create_reservation(email, table_id, date):
        sql = "INSERT INTO Reservation.reservation VALUES ('{}', {}, '{}')".format(email, table_id, date)
        conn = ReservationResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        return res

    @staticmethod
    def delete_reservation(email, table_id):
        sql = "DELETE FROM Reservation.reservation Where email = '{}' and table_id = {}".format(email, table_id)
        conn = ReservationResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        return res

    @staticmethod
    def delete_all_reservation():
        sql = "DELETE FROM Reservation.reservation"
        conn = ReservationResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        return res
