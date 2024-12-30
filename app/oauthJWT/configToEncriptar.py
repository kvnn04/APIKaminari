from dotenv import load_dotenv
from sqlalchemy import Enum
from os import getenv

load_dotenv(dotenv_path='dataSensible.env')

class InfomacionToEncodear(Enum):
    SECRETKEY: str = getenv('SECRET_KEY')
    ALGORITH: str = ['HS256']
    EXPIRETOKEN: int = 50 # min