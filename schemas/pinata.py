from pydantic import BaseModel
from typing import Optional


class PinataBASEMODEL(BaseModel):
    idPiñatas: int
    Nombre_pinata: str
    idTipos_de_piñatas: int
    idFestividades: int
    Precio: float
    Imagen: str
    Id_Tag: Optional[int] = None


class ModifyPinata(BaseModel):
    Nombre_pinata: Optional[str] = None
    idTipos_de_piñatas: Optional[int] = None
    idFestividades: Optional[int] = None
    Precio: Optional[float] = None
    Imagen: Optional[str] = None
    Id_Tag: Optional[int] = None


class MyIDResponse(PinataBASEMODEL):
    idPiñatas: int