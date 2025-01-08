from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

load_dotenv(dotenv_path='dataSensible.env')

# usuario = "root"
# contrasenia = "Kevinherrera.04"                                   SIN LAS VARIABLES .ENV
# host = "localhost"  # o la IP del servidor de tu base de datos
# db = "Kaminari"
# usuario = getenv('USUARIO')
# contrasenia = getenv('CONTRASENIA')
# host = getenv('HOST')
# db = getenv('DB')
url_msql=getenv('URL_MYSQL')
# Crear la URL de conexión para MySQL con mysql-connector-python
engine = create_engine(url=url_msql) # esto requiere de la libreria "mysql-connector-python"
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)