from dao.UsuarioDAO import UsuarioDAO
from dao.AutorDAO import AutorDAO
from dao.LibroDAO import LibroDAO
from dao.PrestamoDAO import PrestamoDAO
from models.Usuario import Usuario
from models.Autor import Autor
from models.Libro import Libro
from models.exceptions import AutenticacionError


def iniciar_sesion_bibliotecario():
    dao = UsuarioDAO()
    id_usuario = input("Ingrese su ID de bibliotecario: ").strip()
    password = input("Ingrese su contraseña: ").strip()
    usuario, msg = dao.autenticar_bibliotecario(id_usuario, password)
    if not usuario:
        raise AutenticacionError(msg)

    print(f"Bienvenido/a {usuario['nombre']}")
    return usuario


def menu_usuarios():
    dao = UsuarioDAO()
    while True:
        print("\n==== Gestión de usuarios ====")
        print("1. Crear usuario\n2. Listar usuarios\n3. Buscar usuario\n4. Actualizar usuario\n5. Eliminar usuario\n6. Cambiar password\n7. Cambiar estado\n0. Volver")
        op = input("Opción: ")
        try:
            if op == "1":
                u = Usuario(
                    input("ID usuario: "),
                    input("Nombre: "),
                    input("Dirección/correo: "),
                    input("Tipo (bibliotecario/suscriptor): "),
                    input("Password: "),
                    input("Estado (activo/inactivo): ") or "activo"
                )
                dao.crear(u)
                print("Usuario creado")
            elif op == "2":
                for u in dao.listar():
                    print(u)
            elif op == "3":
                print(dao.buscar_por_id(input("ID: ")))
            elif op == "4":
                dao.actualizar(input("ID: "), input("Nuevo nombre: "), input(
                    "Nueva dirección: "), input("Nuevo tipo: "))
                print("Usuario actualizado")
            elif op == "6":
                dao.actualizar_password(
                    input("ID: "), input("Nuevo password: "))
                print("Password actualizada")
            elif op == "7":
                dao.actualizar_estado(input("ID: "), input(
                    "Nuevo estado (activo/inactivo): "))
                print("Estado actualizado")
            elif op == "5":
                ok, msg = dao.eliminar(input("ID: "))
                print(msg)
            elif op == "0":
                break
        except Exception as e:
            print(f"Error: {e}")


def menu_autores():
    dao = AutorDAO()
    while True:
        print("\n==== Gestión de autores ====")
        print("1. Crear autor\n2. Listar autores\n3. Buscar autor\n4. Actualizar autor\n5. Eliminar autor\n0. Volver")
        op = input("Opción: ")
        try:
            if op == "1":
                a = Autor(nombre=input("Nombre: "), nacionalidad=input("Nacionalidad: "),
                          fecha_nacimiento=input("Fecha nacimiento (YYYY-MM-DD opcional): ") or None)
                dao.crear(a)
                print("Autor creado")
            elif op == "2":
                for a in dao.listar():
                    print(a)
            elif op == "3":
                print(dao.buscar(input("ID autor: ")))
            elif op == "4":
                dao.actualizar(input("ID: "), input("Nombre: "), input(
                    "Nacionalidad: "), input("Fecha nacimiento: ") or None)
                print("Autor actualizado")
            elif op == "5":
                ok, msg = dao.eliminar(input("ID: "))
                print(msg)
            elif op == "0":
                break
        except Exception as e:
            print(f"Error: {e}")


def menu_libros():
    dao = LibroDAO()
    while True:
        print("\n==== Gestión de libros ====")
        print("1. Crear libro\n2. Listar libros\n3. Buscar libro\n4. Actualizar libro\n5. Eliminar libro\n0. Volver")
        op = input("Opción: ")
        try:
            if op == "1":
                l = Libro(titulo=input("Título: "), isbn=input("ISBN: "), anio_publicacion=input(
                    "Año: "), stock=int(input("Stock: ")), id_autor=input("ID autor: "))
                ok, msg = dao.crear(l)
                print(msg)
            elif op == "2":
                for l in dao.listar():
                    print(l)
            elif op == "3":
                for l in dao.buscar(input("Buscar por id, isbn o título: ")):
                    print(l)
            elif op == "4":
                dao.actualizar(input("ID libro: "), input("Título: "), input(
                    "ISBN: "), input("Año: "), int(input("Stock: ")), input("ID autor: "))
                print("Libro actualizado")
            elif op == "5":
                ok, msg = dao.eliminar(input("ID libro: "))
                print(msg)
            elif op == "0":
                break
        except Exception as e:
            print(f"Error: {e}")


def menu_prestamos():
    dao = PrestamoDAO()
    while True:
        print("\n==== Gestión de préstamos ====")
        print("1. Crear préstamo\n2. Listar préstamos\n3. Listar préstamos por usuario\n4. Devolver préstamo\n5. Cambiar usuario del préstamo\n6. Cambiar libro del préstamo\n7. Listar préstamos activos\n0. Volver")
        op = input("Opción: ")
        try:
            if op == "1":
                ok, msg = dao.crear(input("ID usuario: "), input("ID libro: "))
                print(msg)
            elif op == "2":
                for p in dao.listar():
                    print(p)
            elif op == "3":
                for p in dao.listar_por_usuario(input("ID usuario: ")):
                    print(p)
            elif op == "4":
                ok, msg = dao.devolver(input("ID préstamo: "))
                print(msg)
            elif op == "5":
                ok, msg = dao.cambiar_usuario(
                    input("ID préstamo: "), input("Nuevo ID usuario: "))
                print(msg)
            elif op == "6":
                ok, msg = dao.cambiar_libro(
                    input("ID préstamo: "), input("Nuevo ID libro: "))
                print(msg)
            elif op == "7":
                for p in dao.listar_activos():
                    print(p)
            elif op == "0":
                break
        except Exception as e:
            print(f"Error: {e}")


def main():
    try:
        iniciar_sesion_bibliotecario()
    except AutenticacionError as e:
        print(f"Error de autenticación: {e}")
        return

    while True:
        print("\n==== Sistema Biblioteca ====")
        print("1. Gestión de usuarios\n2. Gestión de autores\n3. Gestión de libros\n4. Gestión de préstamos\n0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_autores()
        elif opcion == "3":
            menu_libros()
        elif opcion == "4":
            menu_prestamos()
        elif opcion == "0":
            print("Hasta luego")
            break


if __name__ == "__main__":
    main()
