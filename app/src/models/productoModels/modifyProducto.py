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


    def modificar(self, id_variante: int, id_producto: int, nuevo_talle: str|None = None, nuevo_color: str|None = None, nuevo_stock: int|None = None): 
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try:
            if not session:
                return None
            
            # Filtramos por el ID de la variante Y por el ID del producto padre
            variante = session.query(ProductoIndumentariaVariante).filter(
                ProductoIndumentariaVariante.id == id_variante,
                ProductoIndumentariaVariante.idProductoIndumentaria == id_producto
            ).first()

            if variante:
                # Solo actualizamos si el valor fue enviado (no es None)
                if nuevo_talle is not None:
                    variante.talle = nuevo_talle
                if nuevo_color is not None:
                    variante.color = nuevo_color
                if nuevo_stock is not None:
                    variante.stock = nuevo_stock
                
                conexionDb.guardarCambiosDb(session)
                return True
            return False
        except Exception as e:
            logException(e)
            return None
        finally:
            conexionDb.cerrarConexion(session)


class ModifiStockProductoIndumentariaInDb:
        
        def modificar_producto_base(self, id_producto: int, nuevo_nombre: str|None = None, nuevo_precio: float|None = None, nueva_descripcion: str|None = None, nuevo_id_categoria: int|None = None):
            conexionDb = ConexionDb()
            session = conexionDb.abrirConexion()
            try:
                if not session:
                    return None
                
                # Buscamos el producto principal por su ID
                producto = session.query(ProductoIndumentaria).filter(
                    ProductoIndumentaria.id == id_producto
                ).first()

                if producto:
                    # Solo actualizamos los campos que no vengan como None
                    if nuevo_nombre is not None:
                        producto.nombre = nuevo_nombre
                    if nuevo_precio is not None:
                        producto.precio = nuevo_precio
                    if nueva_descripcion is not None:
                        producto.descripcion = nueva_descripcion
                    if nuevo_id_categoria is not None:
                        producto.idCategoria = nuevo_id_categoria
                    
                    conexionDb.guardarCambiosDb(session)
                    return True
                
                return False # No se encontró el producto
            except Exception as e:
                logException(e)
                return None
            finally:
                conexionDb.cerrarConexion(session)