from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
# from app.src.models.usuarioModels.createUsuario import Usuario
from app.src.models.usuarioModels.deleteUsuario import DeleteCliente
from app.src.models.usuarioModels.contollerUsuario import ClienteHandler
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends

usuarioDeleteRoute = APIRouter()

@usuarioDeleteRoute.delete('/{id}')
def eliminarUsuario(id: int, user: Annotated[dict, Depends(decodeJWTDepends())]):
    if not user:
        return 'usuario no encontrado'
    
    # version 1 de autorizacion
    if user['username'] != 'kvnn' and user['pwd'] != 'boka': 
        return JSONResponse(content='no estas autorizado', status_code=status.HTTP_401_UNAUTHORIZED)
    
    # Aquí usamos el id que viene por la ruta
    clienteDeleted = DeleteCliente().deleteCliente(clienteId=id)
    
    if not clienteDeleted:
        return clienteDeleted
        
    return clienteDeleted

# Acordarme de Autorizar que yo solo pueda eliminar