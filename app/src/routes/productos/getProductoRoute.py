from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.productoModels.productoController import ProductHandler
 
with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

getProductoRoute: APIRouter = APIRouter()

@getProductoRoute.get('/getProducto')
def getProductoAndVariantesInDB(id: int):
    if not id:
        return status.HTTP_204_NO_CONTENT
    producto = ProductHandler().crearGetProducto().getProductoInDb(id=id)
    if not producto:
        return JSONResponse(content='No existe el producto con ese id', status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=producto, status_code=status.HTTP_202_ACCEPTED)



