from pydantic import BaseModel
from typing import Optional


class Colors_Main_Model(BaseModel):
    Name: Optional[str] = None
    Imagen: Optional[str] = None
    Id_Piñatas: Optional[str] = None


class Colors_Response(Colors_Main_Model):
    Id_color: int