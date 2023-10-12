from pydantic import BaseModel


class ProcesoPedidoRequestModel(BaseModel):
    ID: str
    pedido_idpedido: str
    Anticipo: int
    Pago_Final: str

class ProcesoPedido1Response(ProcesoPedidoRequestModel):
    ID: int
