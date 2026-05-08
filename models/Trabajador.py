from models.Persona import Persona
import hashlib
import os

class Trabajador(Persona):
    def __init__(self, rut = None, nombre = None, direccion = None, usuario:str = None, password:str = None, sueldo:int = None, id:int = None, salt:str = None):
        super().__init__(rut, nombre, direccion)
        self.__usuario = self.validar_usuario(usuario)
        self.__password = password
        self.__salt  = salt
        self.__sueldo = sueldo
        self.__id = id
        
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def password(self):
        return self.__password
    
    @property
    def sueldo(self):
        return self.__sueldo
    
    @property
    def id(self):
        return self.__id
    
    @property
    def salt(self):
        return self.__salt
    
    @usuario.setter
    def usuario(self, value):
        self.__usuario = value
    
    @password.setter
    def password(self, value):
        self.__password = value
        
    @sueldo.setter
    def sueldo(self, value):
        self.__sueldo = value
    
    @id.setter
    def id(self, value):
        self.__id = value
        
    def validar_usuario(self, usuario: str):
        if usuario is None:
            return
        
        if usuario.strip() == "":
            raise ValueError('Nombre de usuario no debe ser vacio')
        elif len(usuario) > 20:
            raise ValueError('Nombre de usuario no puede ser mayor a 10 caracteres')
        
        return usuario
    
    def hash_password(self, password, salt=None):
        if salt is None:
            salt = os.urandom(16)  # Genera una sal aleatoria de 16 bytes
        else:
            salt = salt.encode('utf-8')
        # Combina la contraseña y la sal antes de hashear
        password_hash = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
        return password_hash, salt.hex()

    def verify_password(self, password, stored_password_hash, salt):
        # Recalcula el hash de la contraseña con la misma sal
        new_password_hash = hashlib.sha256(bytes.fromhex(salt) + password.encode('utf-8')).hexdigest()
        # Compara el hash calculado con el hash almacenado
        return new_password_hash == stored_password_hash