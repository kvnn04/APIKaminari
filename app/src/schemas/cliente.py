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
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.session = self.Session()                                         # ES BUENA IDEA DEJARLA ABIERTA?

    def agregarCliente(self, nombre: str|None, apellido: str|None, username: str, email: str, pwd: str):
        try:
            nuevoCliente: Cliente = CreateRegisterCliente(nombre=nombre, apellido=apellido, username=username, email=email, pwd=pwd).crearCliente()
            # Agregar el cliente a la sesión
            self.session.add(nuevoCliente)

            # Confirmar la transacción
            self.session.commit()
        except Exception as e:
            # Si ocurre un error, deshacer la transacción
            logException(e)
            self.session.rollback()
            return 'error en ClientHandler'
        finally:
            # Cerrar la sesión
            self.session.close()
            return 'Nuevo cliente creado con éxito.'

    def consultarClienteInDb(self, username: str, pwd: str):
        try:
            # Obtener un cliente por su ID
            cliente = self.session.query(Cliente).filter(Cliente.username == username, Cliente.pwd == pwd).first()
            if not cliente:
                return "Cliente no encontrado"
            else:
                datosRequired = {'id': cliente.id, 'username': cliente.username, 'pwd': cliente.pwd}
        except Exception as e:
            logException(e)
            self.session.rollback()
            return 'error en ClienteHandler-consultarClienteInDb'
        finally:
            self.session.close()
            # print('cliente encontrado')
            return datosRequired




    # Crear una sesión
Base.metadata.create_all(engine)