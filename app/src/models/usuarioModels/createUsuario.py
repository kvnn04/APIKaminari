from pydantic import BaseModel, model_validator, field_validator, Field

from app.src.models.dbConect import ConexionDb
from app.src.models.usuarioModels.consultarUsuario import GetCLienteInDBForUsenameAndEmail
from app.src.schemas.cliente import Cliente
from app.src.utils.hanlerError import logException
# from app.src.models.usuarioModels.contollerUsuario import ClienteHandler
from fastapi import status

class UsuarioRegister(BaseModel):
    nombre: None|str = Field(None, max_length=50)
    apellido: None|str = Field(None, max_length=50)
    username: str = Field(..., max_length=50)
    email: str = Field(..., max_length=50)
    pwd: str = Field(..., min_length=8)                       # Esto messirve para el futuro, su/ cuando lo veo con lo que hace home voy a entender, su
    verifyPwd: str = Field(...)
    
    @model_validator(mode="after")
    def verifyPassword(self) -> str|ValueError:
        if self.pwd != self.verifyPwd:
            raise ValueError("Las contraseñas no coinciden")
        return self
    
    @field_validator('username')
    def validarUsername(cls, value):
        if " " in value:
            raise ValueError("El nombre de usuario no puede contener espacios")
        return value
    
    @field_validator('email')
    def validarEmail(cls, value):
        if "@" not in value:
            raise ValueError("El nombre de usuario no puede contener espacios")
        return value
    
    @field_validator("pwd")
    def validate_password(cls, value):
        if not any(char.isdigit() for char in value):
            raise ValueError("La contraseña debe contener al menos un número")
        if not any(char.isupper() for char in value):
            raise ValueError("La contraseña debe contener al menos una letra mayúscula")
        if " " in value:
            raise ValueError("La contraseña no puede tener espacios")
        return value

class CreateRegisterCliente:
    # aca iria la contraseña hash

    def crearCliente(self, nombre: str, apellido: str, username: str, email: str, pwd: str):
        # Crear un nuevo cliente
        try:
            conexionDB = ConexionDb()
            session = conexionDB.abrirConexion()

            if not session:
                return None
            if GetCLienteInDBForUsenameAndEmail().consultarClienteForUsernameAndEmail(username=username, email=email):
                return False
            
            nuevoCliente: Cliente = Cliente(
                nombre=nombre,
                apellido=apellido,
                username=username,
                email=email,
                pwd=pwd
            )
            session.add(nuevoCliente)
            conexionDB.guardarCambiosDb(session)
            return True
        except Exception as e:
            logException(e)
            conexionDB.cerrarConexion(session)
            print(e)
            return None

        except Exception as e:
            logException(e)
            return'error en la clase CreateRegisterCliente'
        finally:
            conexionDB.cerrarConexion(session)

        


    
        
# class QueryClient(BaseModel):
#     username: str
#     pwd: str




        
# class ClienteHandler:
#     # Crear una clase de sesión
#     def __init__(self):    
#         # self.Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#         # self.session = self.Session()                                         # ES BUENA IDEA DEJARLA ABIERTA?
#         self.conexionDb = ConexionDb()

#     def agregarCliente(self, nombre: str|None, apellido: str|None, username: str, email: str, pwd: str):
#         session = self.conexionDb.abrirConexion()
#         try:
#             nuevoCliente: Cliente = CreateRegisterCliente(nombre=nombre, apellido=apellido, username=username, email=email, pwd=pwd).crearCliente()
#             # Agregar el cliente a la sesión
#             # self.session.add(nuevoCliente)
#             session.add(nuevoCliente)

#             # Confirmar la transacción
#             # self.session.commit()
#             self.conexionDb.guardarCambiosDb(session)
#         except:
#             self.conexionDb.cerrarConexion(session)
        
#     def consultarClienteInDb(self, username: str, pwd: str):
#         try:
#             session = self.conexionDb.abrirConexion()
#             # Obtener un cliente por su ID
#             cliente = session.query(Cliente).filter(Cliente.username == username, Cliente.pwd == pwd).first()
#             print(cliente)
#             if not cliente:
#                 return None
#             self.conexionDb.guardarCambiosDb(session)
#             datosRequired = {'id': cliente.id, 'username': cliente.username, 'pwd': cliente.pwd}
#             self.conexionDb.cerrarConexion(session)
#             # print('cliente encontrado')
#             return datosRequired
#         except Exception as e:
#             logException(e)
#             print(e,'error en ClienteHandler-consultarClienteInDb')
#             return None
        
    
#     # def modificarCliente(self):
#     #     try:
            
#     #         self.conexionDb.cerrarConexion(session)
#     #     except Exception as e:
#     #         logException(e)
#     #         return 'error en modificar Cliente'
    
#     def modificarCliente(self, cliente_id: int, nuevoNombre: None|str = None, nuevoApellido: None|str = None , nuevoUsername: None|str =None):
#         try:
#             session = self.conexionDb.abrirConexion()
#             # Obtener el registro del cliente
#             cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
#             if not cliente:
#                 return f"Cliente con id {cliente_id} no encontrado."

#             # Modificar los atributos según los parámetros proporcionados
#             if nuevoNombre:
#                 cliente.nombre = nuevoNombre
#             if nuevoApellido:
#                 cliente.apellido = nuevoApellido
#             if nuevoUsername:
#                 cliente.username = nuevoUsername

#             # Confirmar los cambios
#             self.conexionDb.guardarCambiosDb(session)
#             self.conexionDb.cerrarConexion(session)
#             return f"Cliente con id {cliente_id} modificado con éxito."
#         except Exception as e:
#             logException(e)
#             print(e,'error en modificar cliente')
#             return None

#     def eliminarCliente(self, clienteId: int):
#         try:
#             session = self.conexionDb.abrirConexion()
#             clientToDelete=session.query(Cliente).filter(Cliente.id == clienteId).first()
#             session.delete(clientToDelete, synchronize_session=False)
#             self.conexionDb.guardarCambiosDb(Session=session)
#             self.conexionDb.cerrarConexion(Session=session)
#             return 'usuario eliminado con exito'
#         except Exception as e:
#             logException(e)
#             print(e, 'error en eliminar en cliente')
#             return None



    # Crear una sesión
# Base.metadata.create_all(engine)






























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