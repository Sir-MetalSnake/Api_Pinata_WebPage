from pydantic import BaseModel
from typing import Optional

class InventaryBaseModel(BaseModel):
    idInventario: int
    disponibilidad: Optional[int] = None
    Existencia: Optional[int] = None
    Vendido: Optional[int] = None
    Apartado: Optional[int] = None
    Total: Optional[int] = None
    id_Piñatas_inv: int


class InventaryDataModel(BaseModel):
    Existencia: Optional[int] = None
    Vendido: Optional[int] = None
    Apartado: Optional[int] = None
    Total: Optional[int] = None

class InventoryState(BaseModel):
    disponibilidad: Optional[int] = None

class InventaryResponseModel(InventaryBaseModel):
    idInventario:int
