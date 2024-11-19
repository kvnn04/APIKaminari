from typing import Annotated
from fastapi import APIRouter, Depends
from app.src.models.usuarioModels.contollerUsuario import ClienteHandler
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends
from fastapi import status

from app.src.utils.hanlerError import logException

with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

usuarioUpdateRoute = APIRouter()

@usuarioUpdateRoute.put('/modifiUser')
def modificarUsuario(user: Annotated[str, Depends(decodeJWTDepends())], nuevoNombre: str|None = None, nuevoApellido: str|None = None, nuevoUserame: str|None = None):
    try:
        if nuevoNombre or nuevoApellido or nuevoUserame:
            ClienteHandler().crearModifyClient().modify(clienteId=user['id'], nuevoNombre=nuevoNombre, nuevoUsername=nuevoUserame, nuevoApellido=nuevoApellido)
            return status.HTTP_200_OK
        return status.HTTP_204_NO_CONTENT
    except Exception as e:
        logException(e)
        return status.HTTP_500_INTERNAL_SERVER_ERROR