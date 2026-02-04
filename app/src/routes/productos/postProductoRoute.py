from typing import Literal, Annotated
from fastapi import APIRouter, Query, status
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.productoModels.productoController import ProductHandler
from fastapi.responses import JSONResponse
 
postProductoRoute: APIRouter = APIRouter()

@postProductoRoute.post('/')
def createProductoInDb(nombre: str, precio: float, descripcion: str, idCategoria: Literal['1','2']):
    print(idCategoria)
    nuevoProducto: bool = ProductHandler().crearProductoInDb().crearProducto(
        nombre=nombre, 
        precio=precio, 
        descripcion=descripcion, 
        idCategoria=int(idCategoria)
    )
    print(nuevoProducto)
    
    if not nuevoProducto:
        return JSONResponse(content='Error', status_code=status.HTTP_409_CONFLICT)
    
    return JSONResponse(content='Producto creado correctamente', status_code=status.HTTP_201_CREATED)

@postProductoRoute.post('/{idProductoIndumentaria}/variantes')
def createProductoVarianteInDb(idProductoIndumentaria: int, talle: Literal['s', 'm', 'l', 'xl', 'xxl', 'xxxl'], color: str, stock: int):
    # El resto de tu lógica se mantiene igual
    nuevoProductoVarianteInDb = ProductHandler().crearProductoVarianteInDb().crearProductoVariante(
        idProductoIndumentaria = idProductoIndumentaria, 
        talle = talle, 
        color = color.lower(), 
        stock = stock
    )
    
    if not nuevoProductoVarianteInDb:
        return JSONResponse(content='Error al crear la variante', status_code=status.HTTP_409_CONFLICT)
        
    return JSONResponse(content='Se creo una variante del producto', status_code=status.HTTP_200_OK)