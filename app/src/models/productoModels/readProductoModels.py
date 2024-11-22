from app.src.models.dbConect import ConexionDb
from app.src.schemas.producto import ProductoIndumentaria, ProductoIndumentariaVariante
from app.src.utils.hanlerError import logException
from sqlalchemy.orm import joinedload

class ReadProductoIndumentaria:

    def getProductoInDb(self, id: int):
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try: 
            if not session:
                return None
            # cliente = self.session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == self.id, ProductoIndumentariaVariante.idProductoIndumentaria == self.id).first()
            producto = (
            session.query(ProductoIndumentaria)
            .options(joinedload(ProductoIndumentaria.variantes))  # Cargar variantes
            .filter(ProductoIndumentaria.id == id)
            .first()
            )            
            if producto:
                productMappeado = {
                    "id": producto.id,
                    "nombre": producto.nombre,
                    "precio": float(producto.precio),  # Convertir a float si es DECIMAL
                    "descripcion": producto.descripcion,
                    "categoria": producto.categoria.categoria if producto.categoria else None,
                    "variantes": [
                        {
                            "talle": variante.talle,
                            "color": variante.color,
                            "stock": variante.stock,
                        }
                        for variante in producto.variantes
                    ]
                }
                return productMappeado
            return False
        except Exception as e:
            logException(e)
            return None
        finally:
            conexionDb.cerrarConexion(session)

class ReadIfProductoIndumentaria:

    def consultarIfProductoIndumentaria(self, id):
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try: 
            if not session:
                return False
            # cliente = self.session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == self.id, ProductoIndumentariaVariante.idProductoIndumentaria == self.id).first()
            producto = session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == id).first()
            if producto:
                return True
            return False
        except Exception as e:
            logException(e)
            return None
        finally:
            conexionDb.cerrarConexion(session)

class ReadProductoIndumentariaIfExiste:
    def consultarIfProductoIndumentaria(self, id):
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try: 
            if not session:
                return False
            # cliente = self.session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == self.id, ProductoIndumentariaVariante.idProductoIndumentaria == self.id).first()
            producto = session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == id).first()
            if producto:
                return True
            return False
        except Exception as e:
            logException(e)
            return None
        finally:
            conexionDb.cerrarConexion(session)