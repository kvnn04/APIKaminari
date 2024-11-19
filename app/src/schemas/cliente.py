from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from app.config.DBConfig import engine
from app.src.models.dbConect import ConexionDb

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'Cliente'  # El nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    apellido = Column(String(30))
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(100), unique=True)
    pwd = Column(String(200), nullable=False)
    fecha_registro = Column(DateTime, default=func.current_timestamp())  # 'fecha_registro' con valor por defecto de la hora actual

Base.metadata.create_all(engine)