

from pydantic import BaseModel, Field, field_validator, model_validator
from sqlalchemy import or_

from app.src.models.dbConect import ConexionDb
from app.src.schemas.cliente import Cliente
from app.src.utils.hanlerError import logException


class GetCLienteInDB:
    def consultarCliente(self, username: str, pwd: str):
        try:
            conexionDB = ConexionDb()
            session = conexionDB.abrirConexion()
            if session:
                cliente = session.query(Cliente).filter(Cliente.username == username, Cliente.pwd == pwd).first()
                return cliente
            else:
                return None
        except Exception as e:
            logException(e)
            print(e)
            return None
        finally:
            conexionDB.cerrarConexion(session)
    def consultarClienteForEmail(self, email: str, pwd: str):
        try:
            conexionDB = ConexionDb()
            session = conexionDB.abrirConexion()
            if session:
                cliente = session.query(Cliente).filter(Cliente.email == email, Cliente.pwd == pwd).first()
                return cliente
            else:
                return None
        except Exception as e:
            logException(e)
            print(e)
            return None
        finally:
            conexionDB.cerrarConexion(session)

class GetCLienteInDBForUsenameOrEmail:
    def consultarClienteForUsernameOrEmail(self, username: str, email: str):
        try:
            conexionDB = ConexionDb()
            session = conexionDB.abrirConexion()
            if not session:
                print('no hay session en consultarClienteForUsernameAndEmail')
                return None
            
            cliente = session.query(Cliente).filter(or_(Cliente.username == username, Cliente.email == email)).first()
            print(cliente)
            if cliente:
                return True
            return False
        except Exception as e:
            logException(e)
            print(e)
            return None
        finally:
            conexionDB.cerrarConexion(session)



