from pydantic import BaseModel


class ProcesoPedidoRequestModel(BaseModel):
    ID: int
    pedido_idpedido: int
    Anticipo: str
    Pago_Final: str

class ProcesoPedido1Response(ProcesoPedidoRequestModel):
    ID: int
