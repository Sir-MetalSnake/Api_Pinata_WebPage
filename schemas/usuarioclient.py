from pydantic import BaseModel
from typing import Optional

# request model
class UserClientRequestModel(BaseModel):
    usuario: Optional[str] = None
    Correo: Optional[str] = None
    contraseña: Optional[str] = None

class UserClient_Modify_Pass(BaseModel):
    contraseña: str

class UserClientResponseModel(UserClientRequestModel):
    idusuarios: int
