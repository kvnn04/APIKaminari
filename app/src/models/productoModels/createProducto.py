from typing import Literal
from app.src.models.dbConect import ConexionDb
from app.src.schemas.producto import ProductoIndumentaria, ProductoIndumentariaVariante
from app.src.utils.hanlerError import logException
from app.src.models.productoModels.readProductoModels import ReadIfProductoIndumentaria

class CrearProductoIndumentariaInDb:
    def crearProducto(self, nombre: str, precio: float, descripcion: str, idCategoria: Literal[1,2]) -> bool|None:
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try:
            if not session:
                return None
            nuevoProducto = ProductoIndumentaria(nombre = nombre, precio = precio, descripcion = descripcion, idCategoria = idCategoria)
            if nuevoProducto:
                session.add(nuevoProducto)
                conexionDb.guardarCambiosDb(session)
                return True
            return False
        except Exception as e:
            logException(e)
            return None 
        finally:
            conexionDb.cerrarConexion(session)

class CreateProductoIndumentariaVarianteInDb:
    def crearProductoVariante(self,idProductoIndumentaria:int, talle: Literal['s', 'm', 'l', 'xl', 'xxl', 'xxxl'], color: str, stock: int) -> bool|None:
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try:
            if not session:
                return False
            nuevoProducto = ProductoIndumentariaVariante(idProductoIndumentaria = idProductoIndumentaria, talle = talle, color = color, stock = stock)
            session.add(nuevoProducto)
            conexionDb.guardarCambiosDb(session)
            return True
        except Exception as e:
            logException(e)
            return None
        finally:
            conexionDb.cerrarConexion(session)