import os

import mysql.connector
from models.Trabajador import Trabajador
from dao.TrabajadorDAO import TrabajadorDAO
from utils.pdf_usuarios import generar_pdf_usuarios


def crear_trabajador():
    print('==== Registrando Trabajador ====')
    rut = input('Ingrese rut: ')
    nombre = input('Ingrese nombre: ')
    direccion = input('Ingrese direccion: ')
    usuario = input('Ingrese usuario: ')
    password = input('Ingrese password: ')
    sueldo_str = input('Ingrese sueldo: ')

    print('2. Administrador')
    print('3. Trabajador')
    rol_str = input('Ingrese rol: ')

    try:
        sueldo = int(sueldo_str)
    except ValueError:
        print("El sueldo debe ser un número entero.")
        return

    try:
        rol = int(rol_str)
    except ValueError:
        print("El rol debe ser un número entero (2 o 3).")
        return

    # --- Validaciones del modelo (ValueError del modelo) ---
    try:
        trabajador = Trabajador(
            rut=rut,
            nombre=nombre,
            direccion=direccion,
            usuario=usuario,
            password=password,
            sueldo=sueldo,
            id=rol
        )
    except ValueError as e:
        # Aquí llegan las validaciones de Persona/Trabajador (nombre vacío, usuario inválido, etc.)
        print(f"Error en datos del trabajador: {e}")
        return

    dao = None
    try:
        dao = TrabajadorDAO(trabajador)
        dao.crear_trabajador()
    except mysql.connector.Error as e:
        # Excepción específica de mysql.connector
        print(f"Error de base de datos al registrar trabajador: {e}")
    except Exception as e:
        # Cualquier otro error INESPERADO
        print(f"Error inesperado al registrar trabajador: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()


def iniciar_sesion():
    print('==== Datos de usuario ====')
    usuario = input('Ingrese su usuario: ').strip().lower()
    password = input('Ingrese su password: ')

    # 1) Validaciones del modelo (ValueError)
    try:
        trabajador = Trabajador(usuario=usuario, password=password)
    except ValueError as e:
        print(f"Error en los datos ingresados: {e}")
        return

    dao = None
    try:
        # 2) DAO y acceso a BD
        dao = TrabajadorDAO(trabajador)
        if dao.iniciar_sesion():
            print(
                f"Inicio de sesión exitoso. Bienvenido {trabajador.nombre}!")
            input("Presione Enter para ir al menú principal...")
            menu_principal(trabajador)
        else:
            print('Usuario o contraseña incorrectos, intente nuevamente.')
    except mysql.connector.Error as e:
        # Errores propiamente de MySQL (conexión, query, etc.)
        print(f"Error de base de datos al iniciar sesión: {e}")
    except Exception as e:
        # Cualquier cosa inesperada (bug de código, etc.)
        print(f"Se produjo un error inesperado al iniciar sesión: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()


def exportar_usuarios_pdf(trabajador_actual):
    dao = None
    try:
        dao = TrabajadorDAO(trabajador_actual)
        usuarios = dao.listar_todos()

        if not usuarios:
            print("No hay usuarios registrados para exportar.")
            return

        generar_pdf_usuarios(usuarios, "usuarios.pdf")
    except mysql.connector.Error as e:
        print(f"Error de base de datos al listar usuarios: {e}")
    except Exception as e:
        print(f"Error inesperado al generar el PDF: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()


def menu_principal(trabajador: Trabajador):
    while True:
        # Limpiar pantalla
        os.system('cls')
        # Cargamos opciones
        print('==== Menu principal ====')
        print(f'Bienvenido: {trabajador.nombre}')
        if trabajador.id == 2 or trabajador.id == 1:
            print('1. Crear usuarios')
        print('2. Ver datos')
        print('0. Cerrar sesion')

        opcion = input('Ingrese su opcion: ')
        os.system('cls')

        if opcion == '1' and (trabajador.id == 2 or trabajador.id == 1):
            crear_trabajador()
        
        if opcion == '3' and (trabajador.id == 2 or trabajador.id == 1):
            exportar_usuarios_pdf(trabajador)

        elif opcion == '0':
            print(f'Hasta luego {trabajador.nombre}')
            trabajador = None
            break

        input('Presione enter para continuar...')


def menu_inicio_sesion():
    while True:
        # Limpiar pantalla
        os.system('cls')
        # Cargamos opciones
        print('==== Inicio sesion ====')
        print('1. Iniciar sesion')
        print('0. Salir')

        opcion = input('Ingrese su opcion: ')
        os.system('cls')

        if opcion == '1':
            iniciar_sesion()

        input('Presione enter para continuar...')


menu_inicio_sesion()
