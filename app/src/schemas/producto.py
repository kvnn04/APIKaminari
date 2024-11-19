from pydantic import BaseModel
from sqlalchemy import DECIMAL, Column, Enum, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from app.config.DBConfig import engine
from sqlalchemy.orm import sessionmaker, relationship
from app.src.schemas.cliente import ConexionDb

from app.src.utils.hanlerError import logException

Base = declarative_base()

# Tabla CategoriaOfIndumentaria
class CategoriaOfIndumentaria(Base):
    __tablename__ = 'CategoriaOfIndumentaria'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(Enum('ropa superior', 'ropa inferior', name='categoria_enum'), nullable=False)

    # Relación con ProductoIndumentaria
    productos = relationship('ProductoIndumentaria', back_populates='categoria')

# Tabla ProductoIndumentaria
class ProductoIndumentaria(Base):
    __tablename__ = 'ProductoIndumentaria'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)
    precio = Column(DECIMAL, nullable=False)
    descripcion = Column(Text, nullable=False)
    idCategoria = Column(Integer, ForeignKey('CategoriaOfIndumentaria.id'))

    # Relación con CategoriaOfIndumentaria
    categoria = relationship('CategoriaOfIndumentaria', back_populates='productos')
    variantes = relationship('ProductoIndumentariaVariante', back_populates='producto')

# Tabla ProductoIndumentariaVariante
class ProductoIndumentariaVariante(Base):
    __tablename__ = 'ProductoIndumentariaVariante'

    id = Column(Integer, primary_key=True, autoincrement=True)
    talle = Column(Enum('xs', 's', 'm', 'l', 'xl', 'xxl', 'xxxl', name='talle_enum'), nullable=False)
    color = Column(String(10), nullable=True)
    stock = Column(Integer, nullable=False)
    idProductoIndumentaria = Column(Integer, ForeignKey('ProductoIndumentaria.id'))

    # Relación con ProductoIndumentaria
    producto = relationship('ProductoIndumentaria', back_populates='variantes')



# class GetProducto:

#     def __init__(self, session: sessionmaker):
    
#         self.session: sessionmaker = session

#     def getProductoInDb(self, id: int):
#         # cliente = self.session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == self.id, ProductoIndumentariaVariante.idProductoIndumentaria == self.id).first()
#         producto = self.session.query(ProductoIndumentaria).filter(ProductoIndumentaria.id == id, ProductoIndumentaria.variantes.any(ProductoIndumentariaVariante.idProductoIndumentaria == id)).first()
#         if producto:
#             productMappeado = {
#         "id": producto.id,
#         "nombre": producto.nombre,
#         "precio": float(producto.precio),  # Convertir a float si es DECIMAL
#         "descripcion": producto.descripcion,
#         "variantes": [
#             {
#                 "id": variante.id,
#                 "talle": variante.talle,
#                 "color": variante.color,
#                 "stock": variante.stock,
#             }
#             for variante in producto.variantes
#         ]
#     }
#         return productMappeado
    
# class ProductHandler():

#     def __init__(self):
#         self.conexionDb: ConexionDb = ConexionDb()

#     def crearGetProducto(self):
#         try:
#             session : sessionmaker = self.conexionDb.abrirConexion()
#             return GetProducto(session=session)
#         except Exception as e:
#             print(e)
#             logException(e)
#             return None
