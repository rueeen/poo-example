from models.Persona import Persona


class Usuario(Persona):
    TIPOS_VALIDOS = ["bibliotecario", "suscriptor"]

    def __init__(self, id_usuario=None, nombre=None, direccion=None, tipo_usuario=None, password=None, estado="activo", ultimo_acceso=None):
        super().__init__(nombre=nombre, direccion=direccion)
        self.__id_usuario = id_usuario
        self.__tipo_usuario = self.validar_tipo_usuario(tipo_usuario)
        self.__password = password
        self.__estado = estado
        self.__ultimo_acceso = ultimo_acceso

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def tipo_usuario(self):
        return self.__tipo_usuario

    @property
    def password(self):
        return self.__password

    @property
    def estado(self):
        return self.__estado

    @property
    def ultimo_acceso(self):
        return self.__ultimo_acceso

    @id_usuario.setter
    def id_usuario(self, valor):
        self.__id_usuario = valor

    @tipo_usuario.setter
    def tipo_usuario(self, valor):
        self.__tipo_usuario = self.validar_tipo_usuario(valor)

    @password.setter
    def password(self, valor):
        self.__password = valor

    @estado.setter
    def estado(self, valor):
        if valor not in ["activo", "inactivo"]:
            raise ValueError("estado debe ser 'activo' o 'inactivo'")
        self.__estado = valor

    @ultimo_acceso.setter
    def ultimo_acceso(self, valor):
        self.__ultimo_acceso = valor

    def validar_tipo_usuario(self, tipo_usuario):
        if tipo_usuario not in self.TIPOS_VALIDOS:
            raise ValueError(
                "tipo_usuario debe ser 'bibliotecario' o 'suscriptor'")
        return tipo_usuario
