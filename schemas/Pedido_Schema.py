from pydantic import BaseModel


class PedidoBaseModel(BaseModel):
    idpedido: int
    Estatus: str
    Fecha_Inicio: str
    Fecha_Estimada_Final:str
    usuario_cliente_idusuarios: int
    Piñata_idPiñatas: int
    Contacto_idContacto: int


class PedidoResponseModel(PedidoBaseModel):
    idpedido: int