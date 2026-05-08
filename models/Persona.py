class Persona:
    def __init__(self, nombre: str = None, direccion: str = None):
        self.__nombre = self.validar_nombre(nombre)
        self.__direccion = direccion

    @property
    def nombre(self):
        return self.__nombre

    @property
    def direccion(self):
        return self.__direccion

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = self.validar_nombre(valor)

    @direccion.setter
    def direccion(self, valor):
        self.__direccion = valor

    @staticmethod
    def validar_nombre(nombre: str):
        if nombre is None or nombre.strip() == "":
            raise ValueError("El nombre es obligatorio")
        return nombre.strip()
