from app.config.DBConfig import engine
from sqlalchemy import MetaData
from fastapi import APIRouter, Depends
from typing import Annotated
from app.src.depends.decodeJWT import decodeJWTDepends



getDbRoute: APIRouter = APIRouter()

@getDbRoute.get('get/tablasInDb')
def getUserFromDb(user: Annotated[str, Depends(decodeJWTDepends())]) -> list:
    # Reflejar la base de datos
    metadata = MetaData()
    metadata.reflect(bind=engine)
    list_nose = []

    # Listar tablas
    print("Tablas en la base de datos:")
    for table_name in metadata.tables.keys():
        list_nose.append(table_name)
    return list_nose