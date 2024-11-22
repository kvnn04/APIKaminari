from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
# from app.src.schemas.cliente import Cliente
from app.src.models.usuarioModels.createUsuario import UsuarioRegister
from fastapi.responses import JSONResponse
from typing import Annotated
from app.src.utils.hanlerError import logException
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.usuarioModels.contollerUsuario import ClienteHandler
from app.src.models.productoModels.productoController import ProductHandler
from fastapi import HTTPException, status

from app.src.routes.getDBRoute import getDbRoute
from app.src.routes.usuarios.postUsuario import usuarioPostRoute
from app.src.routes.usuarios.getUsuario import usuarioGetRoute
from app.src.routes.usuarios.updateUsuario import usuarioUpdateRoute
from app.src.routes.usuarios.deleteUsuario import usuarioDeleteRoute
from app.src.routes.productos.getProductoRoute import getProductoRoute
from app.src.routes.productos.postProductoRoute import postProductoRoute
from app.src.routes.productos.putProductoRoute import putProductoRoute
from app.src.routes.productos.deleteProductoRoute import deleteProductoRoute

from app.oauthJWT.controllerJwt import JWTContoller

app = FastAPI()
app.include_router(prefix='/dbGet',router=getDbRoute, tags=['Prueba Conexion DB'])
app.include_router(prefix='/post/usuario',router=usuarioPostRoute, tags=['Usuario'])
app.include_router(prefix='/get/usuario',router=usuarioGetRoute, tags=['Usuario'])
app.include_router(prefix='/put/usuario',router=usuarioUpdateRoute, tags=['Usuario'])
app.include_router(prefix='/delete/usuario',router=usuarioDeleteRoute, tags=['Usuario'])
app.include_router(prefix='/get/producto',router=getProductoRoute, tags=['Producto'])
app.include_router(prefix='/post/producto',router=postProductoRoute, tags=['Producto'])
app.include_router(prefix='/put/producto',router=putProductoRoute, tags=['Producto'])
app.include_router(prefix='/delete/producto',router=deleteProductoRoute, tags=['Producto'])


# ------------------------------------------------------------------------------------- # login token
@app.post('/token', tags=['Security'])
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    try:
        userInDb = ClienteHandler().crearGetClienteInDb().consultarCliente(username=form_data.username, pwd=form_data.password)
        if not userInDb or form_data.password != userInDb.pwd:
            print(userInDb)
            # Lanzar un error si no se encuentra el usuario
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas",
                headers={"WWW-Authenticate": "Bearer"},
            )
        payload: dict = {'id': userInDb.id, 'username': userInDb.username, 'pwd': userInDb.pwd}
        token: str = JWTContoller().crearEncodeToken().encodeTheStr(payload=payload)
        return {'access_token': token}  # si uso esto con la clase barer si o si lo tengo que poner en un diccionario y tiene que contener si o si 'access_token' y si o si bien escrito
    except Exception as e:
        logException(e)
        return 'hay error en la url "/token"'

@app.post('/home')
def home(cliente: UsuarioRegister):
    h = ClienteHandler().crearGetClienteInDb().consultarCliente(username=cliente.username, pwd=cliente.pwd)
    print(h)
    return cliente

