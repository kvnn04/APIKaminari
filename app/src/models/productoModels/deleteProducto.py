from app.src.models.dbConect import ConexionDb
from app.src.schemas.producto import ProductoIndumentaria, ProductoIndumentariaVariante
from app.src.utils.hanlerError import logException

class EliminarProductoIndumentariaInDb:
    def eliminarProducto(self, idProducto):
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try:
            if not session:
                return None
            # productoVariante = session.query(ProductoIndumentariaVariante).filter_by(idProductoIndumentaria=idProducto).all()
            #  # esto va a eliminar las variantes tambien, pq le agregue en la relationship el cascade='all, delete'
            producto = session.query(ProductoIndumentaria).filter_by(id=idProducto).first()
            if producto:
                session.delete(producto)
                conexionDb.guardarCambiosDb(session)
                return True
            # producto = session.query(ProductoIndumentaria).filter_by(id=idProducto).first()

            # if producto:
            #     session.delete(producto)
            #     conexionDb.guardarCambiosDb(session)
            return False
        except Exception as e:
            logException(e)
            return None 
        finally:
            conexionDb.cerrarConexion(session)