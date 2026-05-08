from models.Conexion import Conexion


class LibroDAO:
    def __init__(self):
        self.conexion = Conexion()

    def crear(self, libro):
        autor = self.conexion.listar_uno("SELECT id_autor FROM autores WHERE id_autor=%s", (libro.id_autor,))
        if not autor:
            return False, "Autor no existe"
        self.conexion.ejecutar("INSERT INTO libros(titulo,isbn,anio_publicacion,stock,id_autor) VALUES (%s,%s,%s,%s,%s)",
                              (libro.titulo, libro.isbn, libro.anio_publicacion, libro.stock, libro.id_autor))
        return True, "Libro creado"

    def listar(self):
        sql = """SELECT l.*, a.nombre autor FROM libros l JOIN autores a ON l.id_autor=a.id_autor ORDER BY l.titulo"""
        return self.conexion.listar(sql)

    def buscar(self, valor):
        sql = "SELECT * FROM libros WHERE id_libro=%s OR isbn=%s OR titulo LIKE %s"
        return self.conexion.listar(sql, (valor, valor, f"%{valor}%"))

    def actualizar(self, id_libro, titulo, isbn, anio_publicacion, stock, id_autor):
        return self.conexion.ejecutar("UPDATE libros SET titulo=%s,isbn=%s,anio_publicacion=%s,stock=%s,id_autor=%s WHERE id_libro=%s",
                                     (titulo, isbn, anio_publicacion, stock, id_autor, id_libro))

    def eliminar(self, id_libro):
        activo = self.conexion.listar_uno("SELECT COUNT(*) total FROM prestamos WHERE id_libro=%s AND estado='activo'", (id_libro,))
        if activo["total"] > 0:
            return False, "No se puede eliminar: tiene préstamos activos"
        self.conexion.ejecutar("DELETE FROM libros WHERE id_libro=%s", (id_libro,))
        return True, "Libro eliminado"
