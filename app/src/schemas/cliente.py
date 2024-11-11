from typing import Literal
from pydantic import BaseModel, Field, field_validator

class Usuario(BaseModel):
    nombre: str
    apellido: str


class Cliente(Usuario):
    rol: Literal['cliente'] = 'cliente'