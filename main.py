from fastapi import FastAPI, Depends
from app.src.schemas.cliente import Cliente
from fastapi.responses import JSONResponse
from typing import Literal, Annotated
from fastapi.security import OAuth2PasswordRequestForm
from app.src.utils.hanlerError import logException
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.utils.jwtUtils import JWTContoller

app = FastAPI()
@app.post('/home')
def home(cliente: Cliente):
    
    return cliente

@app.post('/token', tags=['Security'])
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    try:
        payload: dict = {'username': form_data.username, 'pwd': form_data.password}
        token: str = JWTContoller().crearEncodeToken().encodeTheStr(payload=payload)
        return {'access_token': token}  # si uso esto con la clase barer si o si lo tengo que poner en un diccionario y tiene que contener si o si 'access_token' y si o si bien escrito
    except Exception as e:
        logException(e)
        return 'hay error en la vista de login'
    
@app.get('/userProfile', tags=['Prueba'])
def intentarAlgo(user: Annotated[str, Depends(decodeJWTDepends())]):
    return {'access_toen': user}
@app.get('/userProduc', tags=['Prueba'])
def intentarAlgo2(user: Annotated[str, Depends(decodeJWTDepends())]):
    boca: str = 'bocaaaaaa'
    return {'access_token': user, 'equipo': boca}