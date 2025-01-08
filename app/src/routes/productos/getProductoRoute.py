from typing import List
from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.productoModels.productoController import ProductHandler
 
with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

getProductoRoute: APIRouter = APIRouter()

@getProductoRoute.get('/getAllProducto')
def getProductoAndVariantesInDB():
    producto = ProductHandler().crearGetProducto().getProductoInDb()
    print(producto)
    if not producto:
        return JSONResponse(content='Error', status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=producto, status_code=status.HTTP_200_OK)

@getProductoRoute.get('/getProducto')
def getProductoAndVariantesInDB(id: int):
    if not id:
        return JSONResponse(content='ID required', status_code=status.HTTP_204_NO_CONTENT)
    producto = ProductHandler().crearGetProducto().getProductoInDbById(id=id)
    print(producto)
    if not producto:
        return JSONResponse(content='No existe el producto con ese id', status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=producto, status_code=status.HTTP_200_OK)

@getProductoRoute.get('/getProductoFilterByTalleAndColor')
def getProductoFilteredByTalleAndColor(id: int, talle: str, color: str):
    if not id:
        return JSONResponse(content='ID required', status_code=status.HTTP_204_NO_CONTENT)
    
    producto = ProductHandler().crearGetProducto().getProductoByTalleAndColor(id=id, talle=talle, color=color)
    if not producto:
        return JSONResponse(content='No existe el producto con ese id', status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=producto, status_code=status.HTTP_200_OK)

@getProductoRoute.get('/getPrecio')
def getPrecio(id: int):
    if not id:
        return JSONResponse(content='ID is required', status_code=status.HTTP_404_NOT_FOUND)
    
    dataPrecio = ProductHandler().crearGetProducto().getPriceByProducto(id=id)

    # if not dataPrecio

    # if dataPrecio is None or dataPrecio is False:
    if not dataPrecio:
        return JSONResponse(content='error en la peticion', status_code=status.HTTP_404_NOT_FOUND)
    else:
        return JSONResponse(content=dataPrecio, status_code=status.HTTP_200_OK)
    
@getProductoRoute.get('/getPriceByListIdProducto')
def getPriceByListIdProducto(ids: List[int]= Query(...)):
    if not ids:
        return JSONResponse(content='ID is required', status_code=status.HTTP_404_NOT_FOUND)
    # idsMappeados = [int(id) for id in ids]
    # print(idsMappeados)
    dataPrecio = ProductHandler().crearGetProducto().getPriceByListIdProducto(ids=ids)
    print(dataPrecio)

    if not dataPrecio:
        return JSONResponse(content='error en la peticion', status_code=status.HTTP_404_NOT_FOUND)
    else:
        return JSONResponse(content=dataPrecio, status_code=status.HTTP_200_OK)
    
@getProductoRoute.get('/verifyIdsProductos')
def verifyIds(ids: List[int] = Query(...)):
    if not ids:
        return JSONResponse(content='ID is required', status_code=status.HTTP_404_NOT_FOUND)
    
    resultVerifyInDb: bool = ProductHandler().crearGetProducto().verifyIdsInDb(ids=ids)
    if not resultVerifyInDb:
        return JSONResponse(content=resultVerifyInDb, status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content=resultVerifyInDb, status_code=status.HTTP_200_OK)

# f = ProductHandler().crearGetProducto().getPriceByListIdProducto(ids=[1,5])
# print(f)