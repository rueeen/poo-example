from models.Conexion import Conexion


class UsuarioDAO:
    def __init__(self):
        self.conexion = Conexion()

    def crear(self, usuario):
        sql = "INSERT INTO usuarios(id_usuario, nombre, direccion, tipo_usuario) VALUES (%s,%s,%s,%s)"
        return self.conexion.ejecutar(sql, (usuario.id_usuario, usuario.nombre, usuario.direccion, usuario.tipo_usuario))

    def listar(self):
        return self.conexion.listar("SELECT * FROM usuarios ORDER BY nombre")

    def buscar_por_id(self, id_usuario):
        return self.conexion.listar_uno("SELECT * FROM usuarios WHERE id_usuario=%s", (id_usuario,))

    def actualizar(self, id_usuario, nombre, direccion, tipo_usuario):
        return self.conexion.ejecutar(
            "UPDATE usuarios SET nombre=%s, direccion=%s, tipo_usuario=%s WHERE id_usuario=%s",
            (nombre, direccion, tipo_usuario, id_usuario)
        )

    def eliminar(self, id_usuario):
        activo = self.conexion.listar_uno("SELECT COUNT(*) total FROM prestamos WHERE id_usuario=%s AND estado='activo'", (id_usuario,))
        if activo["total"] > 0:
            return False, "No se puede eliminar: el usuario tiene préstamos activos"
        self.conexion.ejecutar("DELETE FROM usuarios WHERE id_usuario=%s", (id_usuario,))
        return True, "Usuario eliminado"
