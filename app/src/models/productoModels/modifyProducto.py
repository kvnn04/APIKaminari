from typing import Literal
from app.src.models.dbConect import ConexionDb
from app.src.schemas.producto import ProductoIndumentaria, ProductoIndumentariaVariante
from app.src.utils.hanlerError import logException

class ModifiStockProductoIndumentariaVarianteInDb:
    def modifiStockVariante(self, idIndumentariaProduct: int, talle: Literal['s', 'm', 'l', 'xl', 'xxl', 'xxxl'], color, nuevoStock: int): 
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try:
            if not session:
                return None
            # Obtener la variante específica directamente
            variante = session.query(ProductoIndumentariaVariante).join(ProductoIndumentaria).filter(ProductoIndumentaria.id == idIndumentariaProduct, ProductoIndumentariaVariante.talle == talle, ProductoIndumentariaVariante.color == color).first()

            if variante:
                # Modificar el stock
                variante.stock = nuevoStock
                conexionDb.guardarCambiosDb(session)
                return True
            return False
        except Exception as e:
            logException(e)
            return None
        finally:
            conexionDb.cerrarConexion(session)