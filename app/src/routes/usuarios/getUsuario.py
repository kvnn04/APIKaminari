from typing import Annotated
from fastapi import APIRouter, Depends
from app.src.models.usuario import UsuarioRegister
from app.src.schemas.cliente import ClienteHandler
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends

with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

usuarioGetRoute = APIRouter()

@usuarioGetRoute.get('/getUsuario')
def getUsuarioDb(user: Annotated[str, Depends(decodeJWTDepends())]):
    # print(type(user), 'adsfffffffffffffffffffffffffffffffffffffffffffffffffffff')        
    if not user:
        return 'no existe'
    queryInDb = ClienteHandler().consultarClienteInDb(username=user['username'], pwd=user['pwd'])
    return queryInDb