from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from app.src.models.usuarioModels.contollerUsuario import ClienteHandler
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends
from fastapi import status

from app.src.utils.hanlerError import logException

with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

usuarioUpdateRoute = APIRouter()

@usuarioUpdateRoute.put('/{id}')
def modificarUsuario(id: int, user: Annotated[dict, Depends(decodeJWTDepends())], nuevoNombre: str|None = None, nuevoApellido: str|None = None, nuevoUserame: str|None = None):
    
    # version 1 de autorizacion
    if user['username'] != 'kvnn' and user['pwd'] != 'boka': 
        return JSONResponse(content='no estas autorizado', status_code=status.HTTP_401_UNAUTHORIZED)
    
    try:
        if nuevoNombre or nuevoApellido or nuevoUserame:
            # Usamos el id que pasas por la ruta
            ClienteHandler().crearModifyClient().modify(
                clienteId=id, 
                nuevoNombre=nuevoNombre, 
                nuevoUsername=nuevoUserame, 
                nuevoApellido=nuevoApellido
            )
            return status.HTTP_200_OK
        
        return status.HTTP_204_NO_CONTENT
    except Exception as e:
        logException(e)
        return status.HTTP_500_INTERNAL_SERVER_ERROR