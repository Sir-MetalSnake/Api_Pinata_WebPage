from pydantic import BaseModel
from typing import Optional


# request model
class UserClientRequestModel(BaseModel):
    usuario: str
    Correo: str
    contraseña: str


class UserClientResponseModel(UserClientRequestModel):
    idusuarios: int
