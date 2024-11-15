from datetime import datetime, timedelta, timezone
from jose.jwt import encode, decode
from jose.exceptions import ExpiredSignatureError,JWEInvalidAuth,JWTError,JWTClaimsError
from pydantic import BaseModel
from enum import Enum
from app.src.utils.hanlerError import logException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status


class InfomacionToEncodear(Enum):
    SECRETKEY: str = 'EstaEsMiKey'
    ALGORITH: str = ['HS256']
    EXPIRETOKEN: int = 50 # min


class EncodeToken(BaseModel):
    '''
    Esta clase se encarga de encriptar un JWT
    '''

    def encodeTheStr(self, payload: dict) -> str:
        try:
            expiration = datetime.now(timezone.utc) + timedelta(minutes=InfomacionToEncodear.EXPIRETOKEN.value)
            payload.update({'exp': expiration})

            return encode(
                payload,
                key=InfomacionToEncodear.SECRETKEY.value,
                algorithm=InfomacionToEncodear.ALGORITH.value[0] # para encriptar va en formato str y para desencriptar va en lista
                )
        except JWTError as e:
            logException(e)
            return 'hubo un JWTError en la Clase EncodeToken'
        except Exception as e:
            logException(e)
            return 'hubo un error en la Clase EncodeToken'
        

oathScheme = OAuth2PasswordBearer(tokenUrl='token')
        
        
class DecodeToken(BaseModel):
    '''
    Esta clase se encarga de desencriptar un JWT
    '''
    def decodeToken(self, token: Annotated[str, Depends(oathScheme)]) -> dict:
        try:
            print(token,'GDDDDDDDDDDDDDDDSF')
            if token != 'undefined':
                return decode(
                    token,
                    key=InfomacionToEncodear.SECRETKEY.value,
                    algorithms=InfomacionToEncodear.ALGORITH.value
                )
            return None
        except JWEInvalidAuth as e:
            # return f'Este error no se tendria que mostrar, sino mostrar un messsage cualquiera y mandar el error a otro lado {e}: '
            logException(e)
            print(e,'TokenInvalido')
            return None
        except ExpiredSignatureError as e:
            logException(e)
            print(e, 'JWTExipired')
            return None
        except JWTError as e:
            logException(e)
            print(e, 'error JWError')
            return None
        except Exception as e:
            logException(e)
            print(e, 'errorException')
            return None
        
        
class JWTContoller:
    '''
    se encarga de las creaciones de mis clases JWT
    '''
    def crearEncodeToken(self) -> str|EncodeToken:
        '''
        esta funcion en especifico crea la clase EncodeToken
        '''
        try:
            return EncodeToken()
        except Exception as e:
            logException(e)
            return 'Error en JWTController en la parte de EncodeToken'
        
    def crearDecodeToken(self) -> dict|DecodeToken:
        '''
        esta funcion en especifico crea la clase DecodeToken
        '''
        try:
            return DecodeToken()
        except Exception as e:
            logException(e)
            return 'Error en JWTController en la creacion de DecodeToken'