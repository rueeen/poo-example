class Autor:
    def __init__(self, id_autor=None, nombre=None, nacionalidad=None, fecha_nacimiento=None):
        self.__id_autor = id_autor
        self.__nombre = self.validar_nombre(nombre)
        self.__nacionalidad = nacionalidad
        self.__fecha_nacimiento = fecha_nacimiento

    @property
    def id_autor(self):
        return self.__id_autor

    @property
    def nombre(self):
        return self.__nombre

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @staticmethod
    def validar_nombre(nombre):
        if nombre is None or nombre.strip() == "":
            raise ValueError("El nombre del autor es obligatorio")
        return nombre.strip()
