from pydantic import BaseModel

class OAuth2PwdWithEmailForm(BaseModel):
    password: str
    email: str

