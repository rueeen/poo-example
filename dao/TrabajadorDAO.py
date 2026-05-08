from models.Conexion import Conexion
from models.Trabajador import Trabajador


class TrabajadorDAO:
    def __init__(self, trabajador: Trabajador):
        # Si Conexion() falla, lanzará la excepción y la capa superior la atrapará
        self.__conexion = Conexion()
        self.__trabajador = trabajador

    def iniciar_sesion(self):
        sql_salt = 'SELECT password, salt FROM trabajador WHERE usuario = %s'

        datos = self.__conexion.listar_uno(
            sql_salt, (self.__trabajador.usuario,))

        if not self.__trabajador.verify_password(self.__trabajador.password, datos['password'], datos['salt']):
            print('Credenciales no validas')
            return

        sql = '''
        SELECT p.rut, p.nombre, t.sueldo, p.direccion, t.id
        FROM persona p JOIN trabajador t 
        ON p.rut = t.rut
        WHERE usuario = %s
        '''
        # Ojo: aquí ya NO capturo errores de BD, dejo que suban
        datos = self.__conexion.listar_uno(
            sql,
            (self.__trabajador.usuario, )
        )

        if not datos:
            return False

        self.__trabajador.rut = datos['rut']
        self.__trabajador.sueldo = datos['sueldo']
        self.__trabajador.nombre = datos['nombre']
        self.__trabajador.direccion = datos['direccion']
        self.__trabajador.id = datos['id']
        return True

    def crear_trabajador(self):
        # igual podrías dejar esta lógica como la tienes o adaptarla
        sql_persona = 'INSERT INTO persona(rut, nombre, direccion) VALUES (%s, %s, %s)'
        sql_trabajador = '''
            INSERT INTO trabajador(rut, usuario, id, password, sueldo, salt) 
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        datos_persona = (
            self.__trabajador.rut,
            self.__trabajador.nombre,
            self.__trabajador.direccion
        )
        if not self.__conexion.ejecutar(sql_persona, datos_persona):
            raise RuntimeError('No se logró crear persona (tabla persona).')

        password, salt = self.__trabajador.hash_password(
            self.__trabajador.password)
        print(password, salt)

        datos_trabajador = (
            self.__trabajador.rut,
            self.__trabajador.usuario,
            self.__trabajador.id,
            password,
            self.__trabajador.sueldo,
            salt
        )

        print(datos_trabajador)

        if not self.__conexion.ejecutar(sql_trabajador, datos_trabajador):
            raise RuntimeError(
                'No se logró crear trabajador (tabla trabajador).')

        print('Se creó trabajador')

    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()

    def listar_todos(self):
        sql = '''
        SELECT 
            p.rut,
            p.nombre,
            p.direccion,
            t.usuario,
            t.sueldo,
            t.id
        FROM persona p 
        JOIN trabajador t ON p.rut = t.rut
        ORDER BY p.nombre
        '''
        return self.__conexion.listar(sql)
