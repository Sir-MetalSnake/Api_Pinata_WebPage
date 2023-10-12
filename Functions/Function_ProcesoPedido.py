from MyTables.Proceso_Del_Pedido import ProcesoPedido
from schemas.ProcesoDelPedido import *
from fastapi import HTTPException # REQUEST EXCEPTION

async def get_Proceso_Del_Pedido(ID):
    ProcesoP = ProcesoPedido.select().where(ProcesoPedido.ID == ID)
    if ProcesoP:
        return ProcesoPedido1Response(pedido_idpedido = ProcesoP.pedido_idpedido,
                                      Anticipo = ProcesoP.Anticipo,
                                      Pago_Final = ProcesoP.Pago_Final)
    else:
        raise HTTPException(404, "No se ha encontrado el dato")




async def Create_Procedo_Del_Pedido(Req: ProcesoPedidoRequestModel):
    res = ProcesoPedido.select().where(ProcesoPedido.ID == Req.pedido_idpedido)
    if res:
        raise HTTPException(404,  'Ya hay un objeto con esa clave')
    else:
        Req = ProcesoPedido.create(
            pedido_idpedido=Req.pedido_idpedido,
            Anticipo = Req.Anticipo,
            Pago_Final = Req.Pago_Final
        )
        return Req
