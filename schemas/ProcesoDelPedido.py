from pydantic import BaseModel
from typing import Optional


class ProcesoPedidoRequestModel(BaseModel):
    pedido_idpedido: int
    Anticipo: str
    Pago_Final: Optional[str] = None


class PagoFinalModify(BaseModel):
    Pago_Final: str


class ProcesoPedido1Response(ProcesoPedidoRequestModel):
    ID: int
