from pydantic import BaseModel
from typing import Optional

# request model
class UserClientRequestModel(BaseModel):
    usuario: Optional[str] = None
    Correo: Optional[str] = None
    contraseña: Optional[str] = None
    Nombre: Optional[str] = None
    Apellido_P: Optional[str] = None
    Apellido_M: Optional[str] = None
    Telefono: Optional[str] = None

class UserClient_Modify_Pass(BaseModel):
    contraseña: str


class UserClient_Modify_Tel(BaseModel):
    Telefono: str

class UserClientResponseModel(UserClientRequestModel):
    idusuarios: int
