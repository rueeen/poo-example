from models.Persona import Persona


class Usuario(Persona):
    TIPOS_VALIDOS = ["bibliotecario", "suscriptor"]

    def __init__(self, id_usuario=None, nombre=None, direccion=None, tipo_usuario=None):
        super().__init__(nombre=nombre, direccion=direccion)
        self.__id_usuario = id_usuario
        self.__tipo_usuario = self.validar_tipo_usuario(tipo_usuario)

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def tipo_usuario(self):
        return self.__tipo_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        self.__id_usuario = valor

    @tipo_usuario.setter
    def tipo_usuario(self, valor):
        self.__tipo_usuario = self.validar_tipo_usuario(valor)

    def validar_tipo_usuario(self, tipo_usuario):
        if tipo_usuario not in self.TIPOS_VALIDOS:
            raise ValueError("tipo_usuario debe ser 'bibliotecario' o 'suscriptor'")
        return tipo_usuario
