from typing import Annotated
from fastapi import APIRouter, Depends,status
from fastapi.responses import JSONResponse
# from app.src.models.usuarioModels.consultarUsuario import UsuarioSignIn
from app.src.models.usuarioModels.contollerUsuario import ClienteHandler
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends

with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

usuarioGetRoute = APIRouter()

@usuarioGetRoute.get('/getUsuario')
def getUsuarioDb(user: Annotated[str, Depends(decodeJWTDepends())]):
    if not user:
        return JSONResponse(content='No existe el usuario', status_code=status.HTTP_200_OK)
    queryInDb = ClienteHandler().crearGetClienteInDb().consultarCliente(username=user['username'], pwd=user['pwd'])
    if not queryInDb:
        queryInDb = ClienteHandler().crearGetClienteInDb().consultarClienteForEmail(email=user['username'], pwd=user['pwd'])
        if not queryInDb:
            return status.HTTP_404_NOT_FOUND
        nuevoPayload={'username': queryInDb.username, 'email': queryInDb.email, 'nombre': queryInDb.nombre, 'apellido': queryInDb.apellido, 'exp': user['exp']}
        return JSONResponse(content=nuevoPayload, status_code=status.HTTP_200_OK)
        
    nuevoPayload={'username': queryInDb.username, 'email': queryInDb.email, 'nombre': queryInDb.nombre, 'apellido': queryInDb.apellido, 'exp': user['exp']}
    # payload = {'username': queryInDb.username, 'pwd': queryInDb.pwd}
    return JSONResponse(content=nuevoPayload, status_code=status.HTTP_200_OK)
