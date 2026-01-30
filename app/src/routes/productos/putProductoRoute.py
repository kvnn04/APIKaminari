from typing import Literal, Annotated
from fastapi import APIRouter, Depends, status
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.productoModels.productoController import ProductHandler
from fastapi.responses import JSONResponse
 
with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")

putProductoRoute: APIRouter = APIRouter()

@putProductoRoute.put('/{idProductoIndumentaria}/stock')
def modifiStock(
    idProductoIndumentaria: int, 
    user: Annotated[dict, Depends(decodeJWTDepends())], # Cambiado a dict para acceder a llaves
    id_variante: int, # | None = None # Agregamos esto por si prefieren mandar el ID directo
    talle: Literal['s', 'm', 'l', 'xl', 'xxl', 'xxxl'] | None = None, 
    color: str | None = None, 
    nuevoStock: int | None = None
):
    # Autorización
    if user['username'] != 'kvnn' and user['pwd'] != 'boka':
        return JSONResponse(content='no estas autorizado', status_code=status.HTTP_401_UNAUTHORIZED)
    
    # Llamamos a la nueva función 'modificar'
    # Si no tienes el id_variante, tu lógica de DB debería buscar por los otros filtros
    modifi = ProductHandler().crearModifyStockProductoIndumentaria().modificar(
        id_producto=idProductoIndumentaria,
        id_variante=id_variante, # Puede ser None
        nuevo_talle=talle, 
        nuevo_color=color, 
        nuevo_stock=nuevoStock
    )
    
    if not modifi:
        return JSONResponse(content='No se pudo modificar o no se encontró la variante', status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content='Producto modificado correctamente', status_code=status.HTTP_200_OK)