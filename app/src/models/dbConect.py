from app.src.utils.hanlerError import logException
from sqlalchemy.orm import sessionmaker
from app.config.DBConfig import engine

class ConexionDb:
    # def __init__(self):
    #     self.Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    #     self.session = self.Session()

    def abrirConexion(self):
        try:
            Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            return Session()
        except Exception as e:
            logException(e)
            print(e)
            return None
    
    def guardarCambiosDb(self, Session: sessionmaker):
        try:
            return Session.commit()
        except Exception as e:
            # Si ocurre un error, deshacer la transacción
            logException(e)
            Session.rollback()
            print('error en guardad cambios en la base de datos')
            return None


    def cerrarConexion(self, Session: sessionmaker):
            # Cerrar la sesión
            try: 
                return Session.close()
            except Exception as e:
                logException(e)
                print('hubo un error a la hora de cerrar la conexion a la base de datos')
                return None 