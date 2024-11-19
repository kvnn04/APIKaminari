from typing import Annotated
from fastapi import APIRouter, Depends
from app.src.models.usuarioModels.createUsuario import UsuarioRegister
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.productoModels.producto import ProductHandler
 
with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

productoRoute: APIRouter = APIRouter()

@productoRoute.get('/getProducto')
def getProductoInDb(id: int):
    getProduct = ProductHandler().crearGetProducto()
    productQuery = getProduct.getProductoInDb(id=id)
    return productQuery



