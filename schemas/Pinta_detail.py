from pydantic import BaseModel


class Pinata_detailBASEMODEL(BaseModel):
    idPiñatas_detalles: int
    Tamaño: str
    Colores: str
    Tiempo_estimado: str
    Stock: int
    Piñata_idPiñatas: int


class ModifyPinata_detail(BaseModel):
    Tamaño: str
    Colores: str
    Tiempo_estimado: str
    Stock: int
    Piñata_idPiñatas: int


class MyID_DetailResponse(Pinata_detailBASEMODEL):
    Piñata_idPiñatas: int