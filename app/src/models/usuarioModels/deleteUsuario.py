from app.src.models.dbConect import ConexionDb
from app.src.schemas.cliente import Cliente
from app.src.utils.hanlerError import logException



class DeleteCliente:
    def deleteCliente(self, clienteId: int):
        try:
            conexionDB = ConexionDb()
            session = conexionDB.abrirConexion()
            if session:
                clientToDelete=session.query(Cliente).filter(Cliente.id == clienteId).first()
                session.delete(clientToDelete)  # No uses synchronize_session=False aquí
                conexionDB.guardarCambiosDb(session)
                return True
            else:
                return False
        except Exception as e:
            logException(e)
            print(e)
            return False
        finally:
            conexionDB.cerrarConexion(session)