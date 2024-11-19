from app.oauthJWT.controllerJwt import JWTContoller
from app.src.utils.hanlerError import logException


def decodeJWTDepends() -> dict|str:
    try: 
        # return JWTContoller().crearDecodeToken().decodeToken(token=token) # este esta mal, va sin abrir los parentesis
        return JWTContoller().crearDecodeToken().decodeToken
    except Exception as e:
        logException(e)
        return 'hubo error en la dependencia de decode'