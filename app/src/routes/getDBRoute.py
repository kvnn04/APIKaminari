from fastapi.responses import JSONResponse
from app.config.DBConfig import engine
from sqlalchemy import MetaData
from fastapi import APIRouter, Depends, status
from typing import Annotated
from app.src.depends.decodeJWT import decodeJWTDepends



getDbRoute: APIRouter = APIRouter()

@getDbRoute.get('get/tablasInDb')
def getUserFromDb(user: Annotated[str, Depends(decodeJWTDepends())]) -> list:

    if user['username'] != 'kvnn' and user['pwd'] != 'boka':
        return JSONResponse(content='no estas autorizado', status_code=status.HTTP_401_UNAUTHORIZED)
    

    # Reflejar la base de datos
    metadata = MetaData()
    metadata.reflect(bind=engine)
    list_nose = []

    # Listar tablas
    print("Tablas en la base de datos:")
    for table_name in metadata.tables.keys():
        list_nose.append(table_name)
    return list_nose