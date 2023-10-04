from pydantic import BaseModel
from typing import Optional


class TypeofPinataRequestModel(BaseModel):
    idTipos_de_piñatas: int
    Tipo: str



class TypeofPinataResponseModel(TypeofPinataRequestModel):
    idTipos_de_piñatas: int

