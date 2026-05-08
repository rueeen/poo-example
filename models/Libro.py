class Libro:
    def __init__(self, id_libro=None, titulo=None, isbn=None, anio_publicacion=None, stock=0, id_autor=None):
        self.__id_libro = id_libro
        self.__titulo = self.validar_titulo(titulo)
        self.__isbn = isbn
        self.__anio_publicacion = anio_publicacion
        self.__stock = self.validar_stock(stock)
        self.__id_autor = id_autor

    @property
    def id_libro(self):
        return self.__id_libro

    @property
    def titulo(self):
        return self.__titulo

    @property
    def isbn(self):
        return self.__isbn

    @property
    def anio_publicacion(self):
        return self.__anio_publicacion

    @property
    def stock(self):
        return self.__stock

    @property
    def id_autor(self):
        return self.__id_autor

    @staticmethod
    def validar_titulo(titulo):
        if titulo is None or titulo.strip() == "":
            raise ValueError("El título es obligatorio")
        return titulo.strip()

    @staticmethod
    def validar_stock(stock):
        if int(stock) < 0:
            raise ValueError("El stock no puede ser negativo")
        return int(stock)
