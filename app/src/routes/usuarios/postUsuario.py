from typing import Annotated
from fastapi import APIRouter, Depends
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.usuario import UsuarioRegister
from app.src.schemas.cliente import ClienteHandler
from app.config.DBConfig import engine

with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

usuarioPostRoute = APIRouter()

@usuarioPostRoute.post('/register')
def registerUsuario(usuario: UsuarioRegister):
    crearUserInDB: str = ClienteHandler().agregarCliente(nombre=usuario.nombre, apellido=usuario.apellido, username=usuario.username, email=usuario.email, pwd=usuario.pwd)
    return 'hecho'

@usuarioPostRoute.post('/usuario/iniciarSession')
def singIn(user: Annotated[str, Depends(decodeJWTDepends())]):
    # print(type(user), 'adsfffffffffffffffffffffffffffffffffffffffffffffffffffff')
    if not user:
        return 'no existe'
    queryInDb = ClienteHandler().consultarClienteInDb(username=user['username'], pwd=user['pwd'])
    if not queryInDb:
        return 'no existe el usuario en db'
    return 'session iniciada'