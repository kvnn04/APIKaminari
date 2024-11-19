from pydantic import BaseModel
from sqlalchemy import DECIMAL, Column, Enum, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from app.config.DBConfig import engine
from sqlalchemy.orm import sessionmaker, relationship
from app.src.schemas.cliente import ConexionDb

from app.src.schemas.producto import ProductoIndumentaria, ProductoIndumentariaVariante
from app.src.utils.hanlerError import logException


class GetProducto:

    def __init__(self, session: sessionmaker):
    
        self.session: sessionmaker = session

    def getProductoInDb(self, id: int):
        # cliente = self.session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == self.id, ProductoIndumentariaVariante.idProductoIndumentaria == self.id).first()
        producto = self.session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == id, ProductoIndumentaria.variantes.any(ProductoIndumentariaVariante.idProductoIndumentaria == id)).first()
        if producto:
            productMappeado = {
        "id": producto.id,
        "nombre": producto.nombre,
        "precio": float(producto.precio),  # Convertir a float si es DECIMAL
        "descripcion": producto.descripcion,
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
    
class ProductHandler():

    def __init__(self):
        self.conexionDb: ConexionDb = ConexionDb()

    def crearGetProducto(self):
        try:
            session : sessionmaker = self.conexionDb.abrirConexion()
            return GetProducto(session=session)
        except Exception as e:
            print(e)
            logException(e)
            return None