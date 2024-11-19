


from app.oauthJWT.decodeJwt import DecodeToken
from app.oauthJWT.encodeJwt import EncodeToken
from app.src.utils.hanlerError import logException


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