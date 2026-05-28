from models.Conexion import Conexion


class PrestamoDAO:
    def __init__(self):
        self.conexion = Conexion()

    def crear(self, id_usuario, id_libro):
        usuario = self.conexion.listar_uno(
            "SELECT * FROM usuarios WHERE id_usuario=%s", (id_usuario,))
        if not usuario:
            return False, "Usuario no existe"
        if usuario["tipo_usuario"] != "suscriptor":
            return False, "Solo usuarios suscriptores pueden recibir préstamos"

        libro = self.conexion.listar_uno(
            "SELECT * FROM libros WHERE id_libro=%s", (id_libro,))
        if not libro:
            return False, "Libro no existe"
        if libro["stock"] <= 0:
            return False, "No hay stock disponible"

        try:
            self.conexion.iniciar_transaccion()
            insercion = self.conexion.ejecutar(
                "INSERT INTO prestamos(id_usuario,id_libro,fecha_prestamo,estado) VALUES (%s,%s,CURDATE(),'activo')",
                (id_usuario, id_libro),
                autocommit=False,
            )
            if insercion["rowcount"] != 1:
                raise Exception("No se pudo insertar el préstamo")

            actualizacion = self.conexion.ejecutar(
                "UPDATE libros SET stock = stock - 1 WHERE id_libro=%s",
                (id_libro,),
                autocommit=False,
            )
            if actualizacion["rowcount"] != 1:
                raise Exception("No se pudo actualizar el stock")

            self.conexion.confirmar()
            return True, "Préstamo creado"
        except Exception as e:
            self.conexion.deshacer()
            return False, f"Error al crear préstamo: {e}"

    def listar(self):
        sql = """SELECT p.*,u.nombre usuario,l.titulo libro FROM prestamos p
                 JOIN usuarios u ON p.id_usuario=u.id_usuario JOIN libros l ON p.id_libro=l.id_libro ORDER BY p.id_prestamo DESC"""
        return self.conexion.listar(sql)

    def listar_por_usuario(self, id_usuario):
        return self.conexion.listar("SELECT * FROM prestamos WHERE id_usuario=%s ORDER BY id_prestamo DESC", (id_usuario,))

    def listar_activos(self):
        return self.conexion.listar("SELECT * FROM prestamos WHERE estado='activo'")

    def devolver(self, id_prestamo):
        p = self.conexion.listar_uno(
            "SELECT * FROM prestamos WHERE id_prestamo=%s", (id_prestamo,))
        if not p:
            return False, "Préstamo no existe"
        if p["estado"] == "devuelto":
            return False, "No se puede devolver dos veces"
        self.conexion.ejecutar(
            "UPDATE prestamos SET estado='devuelto', fecha_devolucion=CURDATE() WHERE id_prestamo=%s", (id_prestamo,))
        self.conexion.ejecutar(
            "UPDATE libros SET stock=stock+1 WHERE id_libro=%s", (p["id_libro"],))
        return True, "Préstamo devuelto"

    def cambiar_usuario(self, id_prestamo, nuevo_usuario):
        p = self.conexion.listar_uno(
            "SELECT * FROM prestamos WHERE id_prestamo=%s", (id_prestamo,))
        if not p or p["estado"] != "activo":
            return False, "Solo se puede cambiar usuario en préstamo activo"
        u = self.conexion.listar_uno(
            "SELECT * FROM usuarios WHERE id_usuario=%s", (nuevo_usuario,))
        if not u or u["tipo_usuario"] != "suscriptor":
            return False, "Nuevo usuario inválido o no suscriptor"
        self.conexion.ejecutar(
            "UPDATE prestamos SET id_usuario=%s WHERE id_prestamo=%s", (nuevo_usuario, id_prestamo))
        return True, "Usuario del préstamo actualizado"

    def cambiar_libro(self, id_prestamo, nuevo_libro):
        p = self.conexion.listar_uno(
            "SELECT * FROM prestamos WHERE id_prestamo=%s", (id_prestamo,))
        if not p or p["estado"] != "activo":
            return False, "Solo se puede cambiar libro en préstamo activo"
        l = self.conexion.listar_uno(
            "SELECT * FROM libros WHERE id_libro=%s", (nuevo_libro,))
        if not l or l["stock"] <= 0:
            return False, "Libro nuevo inválido o sin stock"
        self.conexion.ejecutar(
            "UPDATE libros SET stock=stock+1 WHERE id_libro=%s", (p["id_libro"],))
        self.conexion.ejecutar(
            "UPDATE libros SET stock=stock-1 WHERE id_libro=%s", (nuevo_libro,))
        self.conexion.ejecutar(
            "UPDATE prestamos SET id_libro=%s WHERE id_prestamo=%s", (nuevo_libro, id_prestamo))
        return True, "Libro del préstamo actualizado"
