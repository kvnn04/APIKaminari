from app.src.models.dbConect import ConexionDb
from app.src.schemas.cliente import Cliente
from app.src.utils.hanlerError import logException

#  session = self.conexionDb.abrirConexion()
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

class ModifyClientNombreApellidoUsername:
    def modify(self, clienteId: int, nuevoNombre:str|None = None, nuevoApellido: str|None = None, nuevoUsername: str|None = None):
        try:
            conexionDB = ConexionDb()
            session = conexionDB.abrirConexion()
            if session:
                cliente = session.query(Cliente).filter(Cliente.id == clienteId).first()
            if not cliente:
                return f"Cliente con id {clienteId} no encontrado."

            # Modificar los atributos según los parámetros proporcionados
            if nuevoNombre:
                cliente.nombre = nuevoNombre
            if nuevoApellido:
                cliente.apellido = nuevoApellido
            if nuevoUsername:
                cliente.username = nuevoUsername
                
            conexionDB.guardarCambiosDb(session)
            return True
        except Exception as e:
            logException(e)
            print(e)
            return False
        finally:
            conexionDB.cerrarConexion(session)











# class DeleteCliente:
#     def deleteCliente(self, clienteId: int):
#         try:
#             conexionDB = ConexionDb()
#             session = conexionDB.abrirConexion()
#             if session:
#                 clientToDelete=session.query(Cliente).filter(Cliente.id == clienteId).first()
#                 session.delete(clientToDelete)  # No uses synchronize_session=False aquí
#                 conexionDB.guardarCambiosDb(session)
#                 return True
#             else:
#                 return False
#         except Exception as e:
#             logException(e)
#             print(e)
#             return False
#         finally:
#             conexionDB.cerrarConexion(session)