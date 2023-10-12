from MyTables.Pedido import pedido
from schemas.Pedido_Schema import *
from fastapi import HTTPException

async def get_Pedido(ID_Pedido,ID_usuario):


async def Create_Pedido(Req:PedidoBaseModel):
    res = pedido.select().where(pedido.idpedido == Req.idPiñatas)
    if res:
        raise HTTPException(404, 'Ya hay un objeto con esa clave')
    else:
        Req = pedido.create(
            idpedido=Req.idpedido,
            Estatus=Req.Estatus,
            Fecha_Inicio=Req.Fecha_Inicio,
            Fecha_Estimada_Final=Req.Fecha_Estimada_Final,
            Piñata_idPiñatas=Req.Piñata_idPiñatas,
            usuario_cliente_idusuarios=Req.usuario_cliente_idusuarios,
            Contacto_idContacto=Req.Contacto_idContacto
        )
        return Req


async def Delete_Pedido(ID_Pedido,ID_usuario):
    res = pedido.select().where(pedido.idpedido == ID_Pedido and pedido.usuario_cliente_idusuarios == ID_usuario)
    if res:
        res.delete_instance()
    else:
        raise HTTPException(404,"El dato que desea eliminar no existe")