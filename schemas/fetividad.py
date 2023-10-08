from pydantic import BaseModel


class FestividadBaseModel(BaseModel):
    idFestividades: int
    Nombre_festividad: str


class FestividadResponse(FestividadBaseModel):
    idFestividades: int
