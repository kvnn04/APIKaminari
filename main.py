from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
# from app.src.schemas.cliente import Cliente
from app.src.models.usuario import UsuarioRegister
from fastapi.responses import JSONResponse
from typing import Annotated
from app.src.utils.hanlerError import logException
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.schemas.cliente import ClienteHandler

from app.src.routes.getDBRoute import getDbRoute
from app.src.routes.usuarios.postUsuario import usuarioRoute
from app.src.utils.jwtUtils import JWTContoller

app = FastAPI()
app.include_router(prefix='/dbGet',router=getDbRoute, tags=['Prueba Conexion DB'])
app.include_router(prefix='/usuario',router=usuarioRoute, tags=['Usuario'])

# ------------------------------------------------------------------------------------- # login token
@app.post('/token', tags=['Security'])
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    try:
        userInDb = ClienteHandler().consultarClienteInDb(username=form_data.username, pwd=form_data.password)
        if userInDb == 'Cliente no encontrado':
            return 'clienteNoEncontrado'
        payload: dict = {'id': userInDb['id'], 'username': userInDb['username'], 'pwd': userInDb['pwd']}
        token: str = JWTContoller().crearEncodeToken().encodeTheStr(payload=payload)
        return {'access_token': token}  # si uso esto con la clase barer si o si lo tengo que poner en un diccionario y tiene que contener si o si 'access_token' y si o si bien escrito
    except Exception as e:
        logException(e)
        return 'hay error en la url "/token"'



@app.post('/home')
def home(cliente: UsuarioRegister):
    h = ClienteHandler().consultarClienteInDb(username=cliente.username, pwd=cliente.pwd)
    print(h)
    return cliente





