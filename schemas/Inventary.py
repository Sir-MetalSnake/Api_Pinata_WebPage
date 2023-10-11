from pydantic import BaseModel
from typing import Optional

class InventaryBaseModel(BaseModel):
    idInventario: int
    Existencia: Optional[int] = None
    Vendido: Optional[int] = None
    Apartado: Optional[int] = None
    Total: Optional[int] = None
    Piñatas_detalles_idPiñatas_detalles: int


class InventaryDataModel(BaseModel):
    Existencia: Optional[int] = None
    Vendido: Optional[int] = None
    Apartado: Optional[int] = None
    Total: Optional[int] = None


class InventaryResponseModel(InventaryBaseModel):
    idInventario:int
