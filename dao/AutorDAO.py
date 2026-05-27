from models.Conexion import Conexion


class AutorDAO:
    def __init__(self):
        self.conexion = Conexion()

    def crear(self, autor):
        return self.conexion.ejecutar("INSERT INTO autores(nombre,nacionalidad,fecha_nacimiento) VALUES (%s,%s,%s)",
                                      (autor.nombre, autor.nacionalidad, autor.fecha_nacimiento))

    def listar(self):
        return self.conexion.listar("SELECT * FROM autores ORDER BY nombre")

    def buscar(self, id_autor):
        return self.conexion.listar_uno("SELECT * FROM autores WHERE id_autor=%s", (id_autor,))

    def actualizar(self, id_autor, nombre, nacionalidad, fecha_nacimiento):
        return self.conexion.ejecutar("UPDATE autores SET nombre=%s,nacionalidad=%s,fecha_nacimiento=%s WHERE id_autor=%s",
                                      (nombre, nacionalidad, fecha_nacimiento, id_autor))

    def eliminar(self, id_autor):
        rel = self.conexion.listar_uno(
            "SELECT COUNT(*) total FROM libros WHERE id_autor=%s", (id_autor,))
        if rel["total"] > 0:
            return False, "No se puede eliminar: tiene libros asociados"
        self.conexion.ejecutar(
            "DELETE FROM autores WHERE id_autor=%s", (id_autor,))
        return True, "Autor eliminado"
