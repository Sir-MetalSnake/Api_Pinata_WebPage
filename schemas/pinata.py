from pydantic import BaseModel


class PinataBASEMODEL(BaseModel):
    idPiñatas: int
    Nombre_pinata: str
    idTipos_de_piñatas: int
    idFestividades: int
    Precio: float
    Imagen: str


class ModifyPinata(BaseModel):
    Nombre_pinata: str
    idTipos_de_piñatas: int
    idFestividades: int
    Precio: float
    Imagen: str


class MyIDResponse(PinataBASEMODEL):
    idPiñatas: int