from typing import Literal, Annotated
from fastapi import APIRouter, status
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.productoModels.productoController import ProductHandler
from fastapi.responses import JSONResponse
 
with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

putProductoRoute: APIRouter = APIRouter()

@putProductoRoute.put('/modifyStockProducto')
def modifiStock(idProductoIndumentaria: int, talle: Literal['s', 'm', 'l', 'xl', 'xxl', 'xxxl'], color: str, nuevoStock):
    modifi = ProductHandler().crearModifyStockProductoIndumentaria().modifiStockVariante(idIndumentariaProduct=idProductoIndumentaria, talle=talle, color=color, nuevoStock=nuevoStock)
    if not modifi:
        return JSONResponse(content='No se pudo modificar', status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content='Producto modificado', status_code=status.HTTP_200_OK )