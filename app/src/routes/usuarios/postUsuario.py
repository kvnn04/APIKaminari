from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.usuarioModels.createUsuario import UsuarioRegister
from app.src.models.usuarioModels.contollerUsuario import ClienteHandler
from app.config.DBConfig import engine

with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

usuarioPostRoute = APIRouter()

@usuarioPostRoute.post('/register')
def registerUsuario(usuario: UsuarioRegister):

        
    cliente = ClienteHandler().crearInstanciaRegisterCliente().crearCliente(nombre=usuario.nombre, apellido=usuario.apellido, username=usuario.username, email=usuario.email, pwd=usuario.pwd)
    if cliente == False:
        return status.HTTP_501_NOT_IMPLEMENTED
    if cliente == None:
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    return 'hecho'


@usuarioPostRoute.post('/usuario/iniciarSession')
def singIn(user: Annotated[str, Depends(decodeJWTDepends())]):
    # print(type(user), 'adsfffffffffffffffffffffffffffffffffffffffffffffffffffff')

    if not user:
        return 'no existe'
    # queryInDb = ClienteHandler().consultarClienteInDb(username=user['username'], pwd=user['pwd'])
    queryInDb = ClienteHandler().crearGetClienteInDb().consultarCliente(username=user['username'], pwd=user['pwd'])
    if not queryInDb:
        return 'no existe el usuario en db'
    return user