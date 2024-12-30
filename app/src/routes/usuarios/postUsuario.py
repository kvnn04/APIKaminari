from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from app.src.depends.decodeJWT import decodeJWTDepends
# from app.src.models.usuarioModels.consultarUsuario import UsuarioSignIn
from app.src.models.usuarioModels.createUsuario import UsuarioRegister
from app.src.models.usuarioModels.contollerUsuario import ClienteHandler
from app.config.DBConfig import engine
from app.oauthJWT.controllerJwt import EncodeToken
from app.src.utils.hanlerError import logException

with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

usuarioPostRoute = APIRouter()

@usuarioPostRoute.post('/register')
def registerUsuario(usuario: UsuarioRegister):
    try:
        cliente = ClienteHandler().crearInstanciaRegisterCliente().crearCliente(nombre=usuario.nombre, apellido=usuario.apellido, username=usuario.username, email=usuario.email, pwd=usuario.pwd)
        if cliente is False:
                return JSONResponse(
                    content={"detail": "El nombre de usuario o mail ya existen."},
                    status_code=status.HTTP_501_NOT_IMPLEMENTED
                )
        if cliente is None:
            return JSONResponse(
                content={"detail": "Error del servidor al procesar la solicitud."},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return JSONResponse(
                content={"detail": "Usuario registrado exitosamente."},
                status_code=status.HTTP_200_OK
            )
    except Exception as e:
        logException(e)
        return JSONResponse(
            content={"detail": f"Hubo un error inesperado: {str(e)}"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )