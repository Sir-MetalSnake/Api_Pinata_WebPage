from pydantic import BaseModel
from typing import Optional


class Colors_Main_Model(BaseModel):
    Name: str
    Imagen: str
    Id_Piñatas: str


class Colors_Response(Colors_Main_Model):
    Id_color: int