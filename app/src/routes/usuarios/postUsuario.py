from fastapi import APIRouter
from app.src.models.usuario import UsuarioRegister
from app.src.schemas.cliente import ClienteHandler
from app.config.DBConfig import engine

with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

usuarioRoute = APIRouter()

@usuarioRoute.post('/register')
def registerUsuario(usuario: UsuarioRegister):
    crearUserInDB: str = ClienteHandler().agregarCliente(nombre=usuario.nombre, apellido=usuario.apellido, username=usuario.username, email=usuario.email, pwd=usuario.pwd)
    return 'hecho'