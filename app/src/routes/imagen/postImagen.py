from typing import Literal, Annotated
from fastapi import APIRouter, Depends, Query, status
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.productoModels.productoController import ProductHandler
from fastapi.responses import JSONResponse

from app.src.models.imagenModels.controllerImagen import ControllerImagen

postImagenRoute: APIRouter = APIRouter()

@postImagenRoute.post('/')
def crearImagen(url: str = Query(...), id: int = Query(...)):

    if not url:
        return None
    if not id:
        return None
    
    nuevaImagen = ControllerImagen.crearInstanciaNuevaImagen().crearImagen(url=url, idProducto=id)
    if not nuevaImagen:
        return None
    
    return True

@postImagenRoute.put('/')
def cambiarImagenInDb(user: Annotated[dict, Depends(decodeJWTDepends())], idImg: int = Query(...), newUrl: str = Query(...)):

    # 1. Validación de Autorización (siguiendo tu lógica actual)
    if user['username'] != 'kvnn' and user['pwd'] != 'boka':
        return JSONResponse(
            content='No estás autorizado', 
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    if not newUrl:
        return None
    if not idImg:
        return None
    
    # nuevaImagen = ControllerImagen.crearInstanciaNuevaImagen().crearImagen(url=newUrl, idImagen=idImg)
    nuevaImagen = ControllerImagen.crearInstanciaCambiarImagen().cambiarImagenProducto(idImagen=idImg, newUrl=newUrl)
    
    if not nuevaImagen:
        print('problemas en nueva imagen')
        return None
    
    return True