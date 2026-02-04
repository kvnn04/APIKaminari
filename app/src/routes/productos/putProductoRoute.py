from typing import Literal, Annotated
from fastapi import APIRouter, Depends, status
from app.config.DBConfig import engine
from app.src.depends.decodeJWT import decodeJWTDepends
from app.src.models.productoModels.productoController import ProductHandler
from fastapi.responses import JSONResponse

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
    modifi = ProductHandler().crearModifyStockProductoIndumentariaVariante().modificar(
        id_producto=idProductoIndumentaria,
        id_variante=id_variante, # Puede ser None
        nuevo_talle=talle, 
        nuevo_color=color, 
        nuevo_stock=nuevoStock
    )
    
    if not modifi:
        return JSONResponse(content='No se pudo modificar o no se encontró la variante', status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content='Producto modificado correctamente', status_code=status.HTTP_200_OK)

@putProductoRoute.put('/{idProductoIndumentaria}/modificar')
def modificarBase(
    idProductoIndumentaria: int, 
    user: Annotated[dict, Depends(decodeJWTDepends())],
    nombre: str | None = None,
    precio: float | None = None,
    descripcion: str | None = None,
    idCategoria: int | None = None
):
    # 1. Validación de Autorización (siguiendo tu lógica actual)
    if user['username'] != 'kvnn' and user['pwd'] != 'boka':
        return JSONResponse(
            content='No estás autorizado', 
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    
    # 2. Llamada al Handler
    # Asumo que agregaste la función 'modificar_producto_base' en tu ProductHandler
    resultado = ProductHandler().crearModifyStockProductoIndumentaria().modificar_producto_base(
        id_producto=idProductoIndumentaria,
        nuevo_nombre=nombre,
        nuevo_precio=precio,
        nueva_descripcion=descripcion,
        nuevo_id_categoria=idCategoria
    )
    
    # 3. Respuesta según el resultado
    if resultado is None:
        return JSONResponse(
            content='Error interno en la conexión o proceso', 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    if not resultado:
        return JSONResponse(
            content='Producto no encontrado', 
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    return JSONResponse(
        content='Datos del producto actualizados correctamente', 
        status_code=status.HTTP_200_OK
    )