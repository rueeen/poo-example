class Prestamo:
    ESTADOS_VALIDOS = ["activo", "devuelto"]

    def __init__(self, id_prestamo=None, id_usuario=None, id_libro=None, fecha_prestamo=None, fecha_devolucion=None, estado="activo"):
        self.__id_prestamo = id_prestamo
        self.__id_usuario = id_usuario
        self.__id_libro = id_libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion
        self.__estado = self.validar_estado(estado)

    @property
    def estado(self):
        return self.__estado

    @staticmethod
    def validar_estado(estado):
        if estado not in Prestamo.ESTADOS_VALIDOS:
            raise ValueError("estado debe ser 'activo' o 'devuelto'")
        return estado
