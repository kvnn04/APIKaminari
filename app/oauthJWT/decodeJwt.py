from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose.exceptions import ExpiredSignatureError,JWEInvalidAuth,JWTError,JWTClaimsError
from jose.jwt import decode
from app.oauthJWT.configToEncriptar import InfomacionToEncodear

from app.src.utils.hanlerError import logException

oathScheme = OAuth2PasswordBearer(tokenUrl='token')
        
        
class DecodeToken(BaseModel):
    '''
    Esta clase se encarga de desencriptar un JWT
    '''
    def decodeToken(self, token: Annotated[str, Depends(oathScheme)]) -> dict:
        try:
            # print(token,'GDDDDDDDDDDDDDDDSF')
            if token != 'undefined':
                return decode(
                    token,
                    key=InfomacionToEncodear.SECRETKEY,
                    algorithms=InfomacionToEncodear.ALGORITH,
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