from pydantic import BaseModel
from typing import Optional


class Colors_Main_Model(BaseModel):
    Name: Optional[str] = None
    Imagen: Optional[str] = None
    Id_Piñatas: int



class Colors_Response(Colors_Main_Model):
    Id_color: int