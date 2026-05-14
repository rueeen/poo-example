import mysql.connector


class Conexion:
    def __init__(self):
        self.__conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='biblioteca'
        )

    def iniciar_transaccion(self):
        self.__conn.start_transaction()
        return self

    def confirmar(self):
        self.__conn.commit()
        return self

    def deshacer(self):
        self.__conn.rollback()
        return self

    def ejecutar(self, sql, datos=None, autocommit=True):
        cursor = self.__conn.cursor()
        try:
            cursor.execute(sql, datos)
            if autocommit:
                self.__conn.commit()
            return {
                "ok": cursor.rowcount >= 0,
                "lastrowid": cursor.lastrowid,
                "rowcount": cursor.rowcount,
            }
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
