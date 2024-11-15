from typing import Annotated
from fastapi import APIRouter, Depends
from app.src.models.usuario import UsuarioRegister
from app.src.schemas.cliente import ClienteHandler
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends

with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

usuarioUpdateRoute = APIRouter()

@usuarioUpdateRoute.put('/modifiUser')
def modificarUsuario(user: Annotated[str, Depends(decodeJWTDepends())], nuevoNombre: str|None):
    ClienteHandler().modificarCliente(cliente_id=int(user['id']), nuevoNombre=nuevoNombre)
    return 'hecho'