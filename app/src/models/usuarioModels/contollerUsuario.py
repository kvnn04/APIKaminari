from app.src.models.dbConect import ConexionDb
from app.src.models.usuarioModels.createUsuario import CreateRegisterCliente
from app.src.schemas.cliente import Cliente
from app.src.utils.hanlerError import logException
from app.src.models.usuarioModels.consultarUsuario import GetCLienteInDB, GetCLienteInDBForUsenameAndEmail
from app.src.models.usuarioModels.modifyUsuario import ModifyClientNombreApellidoUsername
from app.src.models.usuarioModels.deleteUsuario import DeleteCliente
from abc import ABC, abstractmethod

class ClienteController(ABC):

    def crearInstanciaRegisterCliente():
        pass

    def crearGetClienteInDb():
        pass

    def crearGetClientInDbForUsernameAndEmail():
        pass
    
    def crearModifyClient():
        pass

    def crearDeleteCliente():
        pass

class ClienteHandler:

    def crearInstanciaRegisterCliente(self):
        try:
            return CreateRegisterCliente()
        except Exception as e:
            logException(e)
            print(e)
            return None
        
    def crearGetClienteInDb(self):
        return GetCLienteInDB()
    
    def crearGetClientInDbForUsernameAndEmail(self):
        return GetCLienteInDBForUsenameAndEmail()
    
    def crearModifyClient(self):
        return ModifyClientNombreApellidoUsername()
    
    def crearDeleteCliente(self):
        return DeleteCliente()
    
        
    # def consultarClienteInDb(self, username: str, pwd: str):
    #     try:
    #         session = self.conexionDb.abrirConexion()
    #         # Obtener un cliente por su ID
    #         cliente = session.query(Cliente).filter(Cliente.username == username, Cliente.pwd == pwd).first()
    #         print(cliente)
    #         if not cliente:
    #             return None
    #         self.conexionDb.guardarCambiosDb(session)
    #         datosRequired = {'id': cliente.id, 'username': cliente.username, 'pwd': cliente.pwd}
    #         self.conexionDb.cerrarConexion(session)
    #         # print('cliente encontrado')
    #         return datosRequired
    #     except Exception as e:
    #         logException(e)
    #         print(e,'error en ClienteHandler-consultarClienteInDb')
    #         return None
        
    
    # def modificarCliente(self):
    #     try:
            
    #         self.conexionDb.cerrarConexion(session)
    #     except Exception as e:
    #         logException(e)
    #         return 'error en modificar Cliente'
    
    # def modificarCliente(self, cliente_id: int, nuevoNombre: None|str = None, nuevoApellido: None|str = None , nuevoUsername: None|str =None):
    #     try:
    #         session = self.conexionDb.abrirConexion()
    #         # Obtener el registro del cliente
    #         cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
    #         if not cliente:
    #             return f"Cliente con id {cliente_id} no encontrado."

    #         # Modificar los atributos según los parámetros proporcionados
    #         if nuevoNombre:
    #             cliente.nombre = nuevoNombre
    #         if nuevoApellido:
    #             cliente.apellido = nuevoApellido
    #         if nuevoUsername:
    #             cliente.username = nuevoUsername

    #         # Confirmar los cambios
    #         self.conexionDb.guardarCambiosDb(session)
    #         self.conexionDb.cerrarConexion(session)
    #         return f"Cliente con id {cliente_id} modificado con éxito."
    #     except Exception as e:
    #         logException(e)
    #         print(e,'error en modificar cliente')
    #         return None

    # def eliminarCliente(self, clienteId: int):
    #     try:
    #         session = self.conexionDb.abrirConexion()
    #         clientToDelete=session.query(Cliente).filter(Cliente.id == clienteId).first()
    #         session.delete(clientToDelete, synchronize_session=False)
    #         self.conexionDb.guardarCambiosDb(Session=session)
    #         self.conexionDb.cerrarConexion(Session=session)
    #         return 'usuario eliminado con exito'
    #     except Exception as e:
    #         logException(e)
    #         print(e, 'error en eliminar en cliente')
    #         return None