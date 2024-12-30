from datetime import datetime, timedelta, timezone
from jose import JWTError
from pydantic import BaseModel
from app.src.utils.hanlerError import logException
from jose.jwt import encode
from app.oauthJWT.configToEncriptar import InfomacionToEncodear

class EncodeToken(BaseModel):
    '''
    Esta clase se encarga de encriptar un JWT
    '''

    def encodeTheStr(self, payload: dict) -> str:
        try:
            expiration = datetime.now(timezone.utc) + timedelta(minutes=InfomacionToEncodear.EXPIRETOKEN)
            payload.update({'exp': expiration})

            return encode(
                payload,
                key=InfomacionToEncodear.SECRETKEY,
                algorithm=InfomacionToEncodear.ALGORITH[0] # para encriptar va en formato str y para desencriptar va en lista
                )
        except JWTError as e:
            logException(e)
            return 'hubo un JWTError en la Clase EncodeToken'
        except Exception as e:
            logException(e)
            return 'hubo un error en la Clase EncodeToken'
        
    