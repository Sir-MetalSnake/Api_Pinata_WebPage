from pydantic import BaseModel


class InventaryBaseModel(BaseModel):
    idInventario: int
    Existencia: int
    Vendido: int
    Apartado: int
    Total: int
    Piñatas_detalles_idPiñatas_detalles: int


class InventaryDataModel(BaseModel):
    Existencia: int
    Vendido: int
    Apartado: int
    Total: int


class InventaryResponseModel(InventaryBaseModel):
    idInventario:int
