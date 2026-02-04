from typing import List
from sqlalchemy import and_
from app.src.models.dbConect import ConexionDb
from app.src.schemas.producto import ImagenProducto, ProductoIndumentaria, ProductoIndumentariaVariante
from app.src.utils.hanlerError import logException
from sqlalchemy.orm import joinedload

class ReadProductoIndumentaria:

    def getProductoInDb(self):
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try: 
            if not session:
                return None
            # cliente = self.session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == self.id, ProductoIndumentariaVariante.idProductoIndumentaria == self.id).first()
            productos = (
                        session.query(ProductoIndumentaria)
                        .options(joinedload(ProductoIndumentaria.categoria),joinedload(ProductoIndumentaria.imagenes))  # Carga la relación 'categoria'
                        .all()
                        )   
            conexionDb.guardarCambiosDb(session)
            if productos:
                listaProductosMappeados = []     
                for producto in productos:
                    productMappeado = {
                        "id": producto.id,
                        "nombre": producto.nombre,
                        "precio": float(producto.precio),  # Convertir a float si es DECIMAL
                        "descripcion": producto.descripcion,
                        "categoria": producto.categoria.categoria if producto.categoria else [],
                        'imagenes' : [imagen.imagen for imagen in producto.imagenes] if producto.imagenes else []
                        }
                    productMappeado['imagenes'].sort()
                    listaProductosMappeados.append(productMappeado)
                
                    
                return listaProductosMappeados
            return False
        except Exception as e:
            logException(e)
            return None
        finally:
            conexionDb.cerrarConexion(session)

    def getProductoInDbById(self, id: int):
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try: 
            if not session:
                return None
            # cliente = self.session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == self.id, ProductoIndumentariaVariante.idProductoIndumentaria == self.id).first()
            producto = (
            session.query(ProductoIndumentaria)
            .options(joinedload(ProductoIndumentaria.variantes), joinedload(ProductoIndumentaria.imagenes))  # Cargar variantes
            .filter(ProductoIndumentaria.id == id)
            .first()
            )
            conexionDb.guardarCambiosDb(session)
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
                    ],
                    'imagenes': [imagen.imagen for imagen in producto.imagenes] if producto.imagenes else []
                }
                return productMappeado
            return False
        except Exception as e:
            logException(e)
            return None
        finally:
            conexionDb.cerrarConexion(session)

    def getProductoByTalleAndColor(self, id: int, talle: str, color: str) -> dict|bool|None:
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try:
            if not session:
                return False
            # producto = session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == id, ProductoIndumentariaVariante.idProductoIndumentaria).first()
            producto = (
        session.query(ProductoIndumentaria)
        .options(
            joinedload(ProductoIndumentaria.variantes)
        )
        .filter(
            ProductoIndumentaria.id == id,
            ProductoIndumentaria.variantes.any(
                and_(
                    ProductoIndumentariaVariante.talle == talle,
                    ProductoIndumentariaVariante.color == color
                )
            )
        )
        .first()
    )
            conexionDb.guardarCambiosDb(session)
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
                        }   for variante in producto.variantes if variante.talle == talle and variante.color == color
                    ]
                }
                return productMappeado
        except Exception as e:
            logException(e)
            return None
        finally:
            conexionDb.cerrarConexion(session)

    def getPriceByProducto(self, id: int):
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try:
            if not session:
                return False
            
            precioByProducto = session.query(
                ProductoIndumentaria.precio
            ).filter(
                ProductoIndumentaria.id == id
            ).scalar()
            precioByProducto = float(precioByProducto)
            return precioByProducto

            
        except Exception as e:
            logException(e)
            return None
        
        finally:
            conexionDb.cerrarConexion(session)

    def getPriceByListIdProducto(self, ids: List[int]):
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()
        try:
            if not session:
                return False
            
            # precioByProducto = session.query(
            #     ProductoIndumentaria.precio
            # ).filter(
            #     ProductoIndumentaria.id == id
            # ).scalar()
            # print(precioByProducto)

            productos = session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id.in_(ids)).all()
            conexionDb.guardarCambiosDb(session)

            dataMappeado = []
            for i in productos:
                data = {'id': i.id, 'nombre': i.nombre, 'precio': float(i.precio)}
                dataMappeado.append(data)
            

            return dataMappeado

            
        except Exception as e:
            logException(e)
            return None
        
        finally:
            conexionDb.cerrarConexion(session)

    def verifyIdsInDb(self, ids: List[int]):
        conexionDb = ConexionDb()
        session = conexionDb.abrirConexion()

        try:
            if not session:
                return False

            productos = session.query(ProductoIndumentaria.id).filter(ProductoIndumentaria.id.in_(ids)).all()
            conexionDb.guardarCambiosDb(session)
            if productos:
                respuesta: List[int] = []
                for i in productos:
                    respuesta.append(i[0])
                return respuesta
            
            return False
 
        except Exception as e:
            logException(e)
            return None
        
        finally:
            conexionDb.cerrarConexion(session)