from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

usuario = "root"
contraseña = "Kevinherrera.04"
host = "localhost"  # o la IP del servidor de tu base de datos
db = "Kaminari"

# Crear la URL de conexión para MySQL con mysql-connector-python
engine = create_engine(f"mysql+mysqlconnector://{usuario}:{contraseña}@{host}/{db}") # esto requiere de la libreria "mysql-connector-python"
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)