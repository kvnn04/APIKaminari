from typing import Literal
from app.src.models.dbConect import ConexionDb
from app.src.schemas.producto import ProductoIndumentaria, ProductoIndumentariaVariante, ImagenProducto
from app.src.utils.hanlerError import logException
# from app.src.models.productoModels.readProductoModels import ReadIfProductoIndumentaria

class CrearImagenProductoIndumentariaInDb:
    @staticmethod
    def crearImagen(url: str, idProducto: int) -> bool|None:
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try:
            if not session:
                return None
            nuevoImagen = ImagenProducto(imagen = url, idProductoIndumentaria = idProducto)
            # nuevoProducto = ProductoIndumentaria(nombre = nombre, precio = precio, descripcion = descripcion, idCategoria = idCategoria)
            if nuevoImagen:
                session.add(nuevoImagen)
                conexionDb.guardarCambiosDb(session)
                return True
            return False
        except Exception as e:
            logException(e)
            return None 
        finally:
            conexionDb.cerrarConexion(session)