from typing import Annotated
from fastapi import APIRouter, Depends
from app.src.models.usuario import UsuarioRegister
from app.src.schemas.cliente import ClienteHandler
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends

usuarioDeleteRoute = APIRouter()

@usuarioDeleteRoute.delete('/deleteUsuario')
def eliminarUsuario(user: Annotated[str, Depends(decodeJWTDepends())]):
    if not user:
        return 'usuario no encontrado'
    
    ClienteHandler().eliminarCliente(clienteId=user['id'])
    return 'Usuario Eliminado'