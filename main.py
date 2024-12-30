from os import getenv
from pathlib import Path
from fastapi import FastAPI, Depends, Query
from fastapi.security import OAuth2PasswordRequestForm
# from app.src.schemas.cliente import Cliente
# from app.src.models.usuarioModels.consultarUsuario import UsuarioSignIn
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
from app.src.routes.imagen.postImagen import postImagenRoute
from app.oauthJWT.controllerJwt import JWTContoller

from dotenv import load_dotenv
from os import getenv

# load_dotenv(dotenv_path='dataSensible.env')

# usuario = getenv('USUARIO')




app = FastAPI()
app.include_router(prefix='/dbGet',router=getDbRoute, tags=['Prueba Conexion DB'])
app.include_router(prefix='/usuario',router=usuarioPostRoute, tags=['Usuario'])
app.include_router(prefix='/usuario',router=usuarioGetRoute, tags=['Usuario'])
app.include_router(prefix='/usuario',router=usuarioUpdateRoute, tags=['Usuario'])
app.include_router(prefix='/usuario',router=usuarioDeleteRoute, tags=['Usuario'])
app.include_router(prefix='/producto',router=getProductoRoute, tags=['Producto'])
app.include_router(prefix='/producto',router=postProductoRoute, tags=['Producto'])
app.include_router(prefix='/producto',router=putProductoRoute, tags=['Producto'])
app.include_router(prefix='/producto',router=deleteProductoRoute, tags=['Producto'])
app.include_router(prefix='/images', router=postImagenRoute, tags=['Imagen'])


# ------------------------------------------------------------------------------------- # login token
    
@app.post('/token', tags=['Security'])
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    try:
        userInDb = ClienteHandler().crearGetClienteInDb().consultarCliente(username=form_data.username, pwd=form_data.password)
        if not userInDb or form_data.password != userInDb.pwd:
            userInDb = ClienteHandler().crearGetClienteInDb().consultarClienteForEmail(email=form_data.username, pwd=form_data.password)
            if not userInDb or form_data.password != userInDb.pwd:    
            
            # print(userInDb)
            # Lanzar un error si no se encuentra el usuario
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content="Credenciales inválidas",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            
        payload: dict = {'id': userInDb.id, 'username': userInDb.username, 'pwd': userInDb.pwd}
        token: str = JWTContoller().crearEncodeToken().encodeTheStr(payload=payload)
        return {'access_token': token}  # si uso esto con la clase barer si o si lo tengo que poner en un diccionario y tiene que contener si o si 'access_token' y si o si bien escrito
    except Exception as e:
        logException(e)
        return 'hay error en la url "/token"'

# @app.post('/home')
# def home(cliente: UsuarioRegister):
#     h = ClienteHandler().crearGetClienteInDb().consultarCliente(username=cliente.username, pwd=cliente.pwd)
#     print(h)
#     return cliente


# @app.post('/token', tags=['Security'])
# def login(formData: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     try:
#         userInDb = ClienteHandler().crearGetClienteInDb().consultarClienteForEmail(email=formData.email, pwd=formData.password)
#         if not userInDb or formData.password != userInDb.pwd:
#             print(userInDb)
#             # Lanzar un error si no se encuentra el usuario
#             return JSONResponse(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 content="Credenciales inválidas",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
#         payload: dict = {'id': userInDb.id, 'email': userInDb.email, 'pwd': userInDb.pwd}
#         token: str = JWTContoller().crearEncodeToken().encodeTheStr(payload=payload)
#         # return {'access_token': f"Bearer: {token}"}  # si uso esto con la clase barer si o si lo tengo que poner en un diccionario y tiene que contener si o si 'access_token' y si o si bien escrito
#         # return JSONResponse(headers={'Authorization': f'Bearer: {token}'})
#         return {"access_token": token, "token_type": "Bearer"}
#     except Exception as e:
#         logException(e)
#         return 'hay error en la url "/token"'
# @app.post('/tokenn', tags=['Security'])
# def login2(formData: Annotated[UsuarioLogin, Depends()]):
#     try:
#         userInDb = ClienteHandler().crearGetClienteInDb().consultarClienteForEmail(email=formData.email, pwd=formData.pwd)
#         if not userInDb or formData.pwd != userInDb.pwd:
#             print(userInDb)
#             # Lanzar un error si no se encuentra el usuario
#             return JSONResponse(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 content="Credenciales inválidas",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
#         payload: dict = {'id': userInDb.id, 'email': userInDb.email, 'pwd': userInDb.pwd}
#         token: str = JWTContoller().crearEncodeToken().encodeTheStr(payload=payload)
#         # return {'access_token': f"Bearer: {token}"}  # si uso esto con la clase barer si o si lo tengo que poner en un diccionario y tiene que contener si o si 'access_token' y si o si bien escrito
#         # return JSONResponse(headers={'Authorization': f'Bearer: {token}'})
#         return {"access_token": token, "token_type": "Bearer"}
#     except Exception as e:
#         logException(e)
#         return 'hay error en la url "/token"'