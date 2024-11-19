from sqlalchemy import Enum


class InfomacionToEncodear(Enum):
    SECRETKEY: str = 'EstaEsMiKey'
    ALGORITH: str = ['HS256']
    EXPIRETOKEN: int = 50 # min