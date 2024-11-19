from typing import Annotated
from fastapi import APIRouter, Depends,status
from app.src.models.usuarioModels.contollerUsuario import ClienteHandler
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends

with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

usuarioGetRoute = APIRouter()

@usuarioGetRoute.get('/getUsuario')
def getUsuarioDb(user: Annotated[str, Depends(decodeJWTDepends())]):
    # print(type(user), 'adsfffffffffffffffffffffffffffffffffffffffffffffffffffff')   
    print(user)     
    if not user:
        return 'no existe'
    
    queryInDb = ClienteHandler().crearGetClienteInDb().consultarCliente(username=user['username'], pwd=user['pwd'])
    if not queryInDb:
        return status.HTTP_404_NOT_FOUND
    return queryInDb