from typing import Literal
from app.src.models.dbConect import ConexionDb
from app.src.schemas.producto import ProductoIndumentaria, ProductoIndumentariaVariante, ImagenProducto
from app.src.utils.hanlerError import logException
# from app.src.models.productoModels.readProductoModels import ReadIfProductoIndumentaria

class CambiarImagenInDb:
    @staticmethod
    def cambiarImagenProducto(idImagen: int, newUrl: str) -> bool|None:
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try:
            if not session:
                return None
            # nuevoImagen = ImagenProducto(imagen = url, idProductoIndumentaria = idProducto)
            nuevoImagen = session.query(ImagenProducto).filter(ImagenProducto.id == idImagen).first()
            # nuevoProducto = ProductoIndumentaria(nombre = nombre, precio = precio, descripcion = descripcion, idCategoria = idCategoria)
            if nuevoImagen:
                nuevoImagen.imagen = newUrl
                conexionDb.guardarCambiosDb(session)
                return True
            return False
        except Exception as e:
            logException(e)
            return None 
        finally:
            conexionDb.cerrarConexion(session)

'''
 variante = session.query(ProductoIndumentariaVariante).join(ProductoIndumentaria).filter(ProductoIndumentaria.id == idIndumentariaProduct, ProductoIndumentariaVariante.talle == talle, ProductoIndumentariaVariante.color == color).first()

            if variante:
                # Modificar el stock
                variante.stock = nuevoStock
                conexionDb.guardarCambiosDb(session)
                return True
'''