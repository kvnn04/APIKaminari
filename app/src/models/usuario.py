from pydantic import BaseModel, model_validator

class UsuarioRegister(BaseModel):
    nombre: None|str = None
    apellido: None|str = None
    username: str
    email: str
    pwd: str
    verifyPwd: str
    
    @model_validator(mode="after")
    def verifyPassword(self) -> str|ValueError:
        if self.pwd != self.verifyPwd:
            raise ValueError("Las contraseñas no coinciden")
        return self































# from abc import ABC,abstractmethod
# class Usuario(ABC):

#     '''
#     PROPIEDADES:
#     USERNAME
#     EMAIL
#     '''

#     @property
#     @abstractmethod
#     def username():           # con fastapi si o si tiene que heredar de BaseModel de pydantic
#         return
    
#     @property
#     @abstractmethod
#     def email():
#         return
    



#     @property
#     @abstractmethod
#     def nombre():
#         return
    
#     @abstractmethod
#     def saludar():
#         return
    
# class Cliente(Usuario):
#     def __init__(self, nombre: str):
#         self._nombre = nombre

#     @property
#     def nombre(self):
#         return self._nombre                   EJEMPLO DE COMO SE IMPLEMENTA UNA CLASE ABSTRACTA
#                                               y cuando lo use en una subclase los atributos van en privado
    
#     def saludar(self):
#         return f'buen dia {self._nombre}'

# hola = Cliente('kevin')
# print(hola.nombre)