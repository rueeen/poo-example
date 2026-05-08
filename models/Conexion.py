import mysql.connector


class Conexion:
    def __init__(self):
        self.__conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='biblioteca'
        )

    def ejecutar(self, sql, datos=None):
        cursor = self.__conn.cursor()
        try:
            cursor.execute(sql, datos)
            self.__conn.commit()
            return cursor.lastrowid, cursor.rowcount
        finally:
            cursor.close()

    def listar(self, sql, datos=None):
        cursor = self.__conn.cursor(dictionary=True)
        try:
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cursor.close()

    def listar_uno(self, sql, datos=None):
        cursor = self.__conn.cursor(dictionary=True)
        try:
            cursor.execute(sql, datos)
            return cursor.fetchone()
        finally:
            cursor.close()

    def cerrar_conexion(self):
        if self.__conn.is_connected():
            self.__conn.close()
