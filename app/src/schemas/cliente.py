from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from app.config.DBConfig import engine
from sqlalchemy.orm import sessionmaker

from app.src.utils.hanlerError import logException

# Crear la clase base para los modelos
Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'Cliente'  # El nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True)  # Definir la columna 'id' como primary key
    nombre = Column(String(30))
    apellido = Column(String(30))
    username = Column(String(30), unique=True, nullable=False)  # 'username' único y no nulo
    email = Column(String(100), unique=True)
    pwd = Column(String(200), nullable=False)  # 'pwd' no nulo
    fecha_registro = Column(DateTime, default=func.current_timestamp())  # 'fecha_registro' con valor por defecto de la hora actual

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
            return 'hubo error en abrir la conexion a la base de datos'
    
    def guardarCambiosDb(self, Session: sessionmaker):
        try:
            return Session.commit()
        except Exception as e:
            # Si ocurre un error, deshacer la transacción
            logException(e)
            Session.rollback()
            return 'error en guardad cambios en la base de datos'


    def cerrarConexion(self, Session: sessionmaker):
            # Cerrar la sesión
            try: 
                return Session.close()
            except Exception as e:
                logException(e)
                return 'hubo un error a la hora de cerrar la conexion a la base de datos' 



class CreateRegisterCliente(BaseModel):

    nombre: str|None
    apellido: str|None
    username: str
    email: str
    pwd: str

    def crearCliente(self):
        try:
            # Crear un nuevo cliente
            return Cliente(
                nombre=self.nombre,
                apellido=self.apellido,
                username=self.username,
                email=self.email,
                pwd=self.pwd
            )

        except Exception as e:
            logException(e)
            return'error en la clase CreateRegisterCliente'

    
        
# class QueryClient(BaseModel):
#     username: str
#     pwd: str




        
class ClienteHandler:
    # Crear una clase de sesión
    def __init__(self):    
        # self.Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        # self.session = self.Session()                                         # ES BUENA IDEA DEJARLA ABIERTA?
        self.conexionDb = ConexionDb()

    def agregarCliente(self, nombre: str|None, apellido: str|None, username: str, email: str, pwd: str):
        session = self.conexionDb.abrirConexion()
        try:
            nuevoCliente: Cliente = CreateRegisterCliente(nombre=nombre, apellido=apellido, username=username, email=email, pwd=pwd).crearCliente()
            # Agregar el cliente a la sesión
            # self.session.add(nuevoCliente)
            session.add(nuevoCliente)

            # Confirmar la transacción
            # self.session.commit()
            self.conexionDb.guardarCambiosDb(session)
        except:
            self.conexionDb.cerrarConexion(session)
        
    def consultarClienteInDb(self, username: str, pwd: str):
        try:
            session = self.conexionDb.abrirConexion()
            # Obtener un cliente por su ID
            cliente = session.query(Cliente).filter(Cliente.username == username, Cliente.pwd == pwd).first()
            print(cliente)
            if not cliente:
                return None
            self.conexionDb.guardarCambiosDb(session)
            datosRequired = {'id': cliente.id, 'username': cliente.username, 'pwd': cliente.pwd}
            self.conexionDb.cerrarConexion(session)
            # print('cliente encontrado')
            return datosRequired
        except Exception as e:
            logException(e)
            print(e,'error en ClienteHandler-consultarClienteInDb')
            return None
        
    
    # def modificarCliente(self):
    #     try:
            
    #         self.conexionDb.cerrarConexion(session)
    #     except Exception as e:
    #         logException(e)
    #         return 'error en modificar Cliente'
    
    def modificarCliente(self, cliente_id: int, nuevoNombre: None|str = None, nuevoApellido: None|str = None , nuevoUsername: None|str =None):
        try:
            session = self.conexionDb.abrirConexion()
            # Obtener el registro del cliente
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            if not cliente:
                return f"Cliente con id {cliente_id} no encontrado."

            # Modificar los atributos según los parámetros proporcionados
            if nuevoNombre:
                cliente.nombre = nuevoNombre
            if nuevoApellido:
                cliente.apellido = nuevoApellido
            if nuevoUsername:
                cliente.username = nuevoUsername

            # Confirmar los cambios
            self.conexionDb.guardarCambiosDb(session)
            self.conexionDb.cerrarConexion(session)
            return f"Cliente con id {cliente_id} modificado con éxito."
        except Exception as e:
            logException(e)
            print(e,'error en modificar cliente')
            return None

    def eliminarCliente(self, clienteId: int):
        try:
            session = self.conexionDb.abrirConexion()
            clientToDelete=session.query(Cliente).filter(Cliente.id == clienteId).first()
            session.delete(clientToDelete, synchronize_session=False)
            self.conexionDb.guardarCambiosDb(Session=session)
            self.conexionDb.cerrarConexion(Session=session)
            return 'usuario eliminado con exito'
        except Exception as e:
            logException(e)
            print(e, 'error en eliminar en cliente')
            return None



    # Crear una sesión
Base.metadata.create_all(engine)