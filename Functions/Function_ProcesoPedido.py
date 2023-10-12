from MyTables.Proceso_Del_Pedido import proceso_del_pedido
from schemas.ProcesoDelPedido import *
from fastapi import HTTPException # REQUEST EXCEPTION

async def get_Proceso_Del_Pedido(ID):
    ProcesoP = proceso_del_pedido.select().where(proceso_del_pedido.ID == ID).first()
    if ProcesoP:
        return ProcesoPedido1Response(ID=ProcesoP.ID,
                                      pedido_idpedido=ProcesoP.pedido_idpedido,
                                      Anticipo=ProcesoP.Anticipo,
                                      Pago_Final=ProcesoP.Pago_Final)
    else:
        raise HTTPException(404, "No se ha encontrado el dato")




async def Create_Procedo_Del_Pedido(Req: ProcesoPedidoRequestModel):
    res = proceso_del_pedido.select().where(proceso_del_pedido.ID == Req.pedido_idpedido)
    if res:
        raise HTTPException(404,  'Ya hay un objeto con esa clave')
    else:
        Req = proceso_del_pedido.create(
            ID=Req.ID,
            pedido_idpedido=Req.pedido_idpedido,
            Anticipo = Req.Anticipo,
            Pago_Final = Req.Pago_Final
        )
        return Req
