# pip install mysql-connector-python
import mysql.connector

class Conexion:
    def __init__(self):
        try:
            self.__conn = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='gestion'
            )
        except mysql.connector.Error as e:
            # Log (opcionales) + relanzar
            print(f'Error de conexión: {e}')
            raise  # sube a TrabajadorDAO y luego a iniciar_sesion
        
    # Sirve para INSERT, UPDATE, DELETE
    def ejecutar(self, sql: str, datos=None):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql, datos)
            self.__conn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as e:
            print(f'Error al ejecutar SQL: {e}')
            raise
        finally:
            cursor.close()
    
    def listar(self, sql: str, datos=None):
        try:
            cursor = self.__conn.cursor(dictionary=True)
            if datos:
                cursor.execute(sql, datos)
            else:
                cursor.execute(sql)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f'Error al listar: {e}')
            raise
        finally:
            cursor.close()
    
    def listar_uno(self, sql: str, datos=None):
        try:
            cursor = self.__conn.cursor(dictionary=True)
            cursor.execute(sql, datos)
            return cursor.fetchone()
        except mysql.connector.Error as e:
            print(f'Error al listar uno: {e}')
            raise
        finally:
            cursor.close()

    def cerrar_conexion(self):
        if self.__conn is not None:
            if self.__conn.is_connected():
                self.__conn.close()