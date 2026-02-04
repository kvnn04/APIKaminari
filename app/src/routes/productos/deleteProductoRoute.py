from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.productoModels.productoController import ProductHandler
 

deleteProductoRoute: APIRouter = APIRouter()

@deleteProductoRoute.delete('/{id}')
def getProductoInDB(id: int, user: Annotated[str, Depends(decodeJWTDepends())]):
    if not id:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    
    if not user:
        return JSONResponse(content=user, status_code=status.HTTP_404_NOT_FOUND)
    
    if user['username'] != 'kvnn' and user['pwd'] != 'boka':
        return JSONResponse(content='no estas autorizado', status_code=status.HTTP_401_UNAUTHORIZED)
    
    producto = ProductHandler().crearEliminarProductoIndumentaria().eliminarProducto(idProducto=id)
    
    if not producto:
        return JSONResponse(content='Producto no encontrado', status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content=producto, status_code=status.HTTP_202_ACCEPTED)




