from pydantic import BaseModel
from typing import Optional

#Request model


class InfoClientRequestModel(BaseModel):
    Nombre: str
    Apellido_P: str
    Apellido_M: str
    telefono: str
    usuario_cliente_idusuarios: int

class InfoClient_Modify_Tel(BaseModel):
    telefono:str

class InfoClienteResponse(InfoClientRequestModel):
    id_info_cliente:int