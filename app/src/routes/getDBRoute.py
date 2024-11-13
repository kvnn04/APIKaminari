from app.config.DBConfig import engine
from sqlalchemy import MetaData
from fastapi import APIRouter, Depends
from typing import Annotated
from app.src.depends.decodeJWT import decodeJWTDepends




with engine.connect() as connection:
    print("Conexión exitosa a la base de datos")


getDbRoute: APIRouter = APIRouter()

@getDbRoute.get('get/user')
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


@getDbRoute.get('/userInDb', tags=['Prueba'])
def intentarAlgo(user: Annotated[str, Depends(decodeJWTDepends())]):
    return {'access_token': user}                                           
@getDbRoute.get('/userProduc', tags=['Prueba'])
def intentarAlgo2(user: Annotated[str, Depends(decodeJWTDepends())]):
    boca: str = 'bocaaaaaa'
    return {'access_toen': user, 'equipo': boca}