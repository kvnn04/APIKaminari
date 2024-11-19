from typing import Annotated
from fastapi import APIRouter, Depends
from app.src.models.usuarioModels.createUsuario import UsuarioRegister
from app.src.models.usuarioModels.deleteUsuario import DeleteCliente
from app.src.models.usuarioModels.contollerUsuario import ClienteHandler
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends

usuarioDeleteRoute = APIRouter()

@usuarioDeleteRoute.delete('/deleteUsuario')
def eliminarUsuario(user: Annotated[str, Depends(decodeJWTDepends())]):
    if not user:
        return 'usuario no encontrado'
    clienteDeleted = DeleteCliente().deleteCliente(clienteId=user['id'])
    if not clienteDeleted:
        return clienteDeleted
    return clienteDeleted

# Acordarme de Autorizar que yo solo pueda eliminar