import json

from MyTables.Pedido import pedido
from schemas.Pedido_Schema import *
from fastapi import HTTPException

async def get_Pedidos_user(ID_usuario):
    pin = pedido.select().where(pedido.usuario_cliente_idusuarios == ID_usuario and pedido.Estatus == 'Pendiente')
    if pin:
        resul = []
        for index in pin:
            Pedi = PedidoResponseModel(idpedido=index.idpedido,
                                       Estatus=index.Estatus,
                                       Fecha_Inicio=index.Fecha_Inicio,
                                       Fecha_Estimada_Final=index.Fecha_Estimada_Final,
                                       Piñata_idPiñatas=index.Piñata_idPiñatas,
                                       usuario_cliente_idusuarios=index.usuario_cliente_idusuarios,
                                       Contacto_idContacto=index.Contacto_idContacto)
            model = {'idpedido': Pedi.idpedido, 'Estatus': Pedi.Estatus,
                     'Fecha_Inicio': Pedi.Fecha_Inicio, 'Fecha_Estimada_Final': Pedi.Fecha_Estimada_Final,
                     'Piñata_idPiñatas': Pedi.Piñata_idPiñatas,
                     'usuario_cliente_idusuarios': Pedi.usuario_cliente_idusuarios,
                     'Contacto_idContacto': Pedi.Contacto_idContacto}
            resul.append(model)
        json_resul = json.dumps({'Pedidos': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")

async def get_Pedidos_user_notify(ID_usuario):
    pin = pedido.select().where(pedido.usuario_cliente_idusuarios == ID_usuario and pedido.Estatus == 'listo')
    if pin:
        resul = []
        for index in pin:
            Pedi = PedidoResponseModel(idpedido=index.idpedido,
                                       Estatus=index.Estatus,
                                       Fecha_Inicio=index.Fecha_Inicio,
                                       Fecha_Estimada_Final=index.Fecha_Estimada_Final,
                                       Piñata_idPiñatas=index.Piñata_idPiñatas,
                                       usuario_cliente_idusuarios=index.usuario_cliente_idusuarios,
                                       Contacto_idContacto=index.Contacto_idContacto)
            model = {'idpedido': Pedi.idpedido, 'Estatus': Pedi.Estatus,
                     'Fecha_Inicio': Pedi.Fecha_Inicio, 'Fecha_Estimada_Final': Pedi.Fecha_Estimada_Final,
                     'Piñata_idPiñatas': Pedi.Piñata_idPiñatas,
                     'usuario_cliente_idusuarios': Pedi.usuario_cliente_idusuarios,
                     'Contacto_idContacto': Pedi.Contacto_idContacto}
            resul.append(model)
        json_resul = json.dumps({'Pedidos': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")

async def get_Pedidos_user_finalizado(ID_usuario):
    pin = pedido.select().where(pedido.usuario_cliente_idusuarios == ID_usuario and pedido.Estatus == 'pagado')
    if pin:
        resul = []
        for index in pin:
            Pedi = PedidoResponseModel(idpedido=index.idpedido,
                                       Estatus=index.Estatus,
                                       Fecha_Inicio=index.Fecha_Inicio,
                                       Fecha_Estimada_Final=index.Fecha_Estimada_Final,
                                       Piñata_idPiñatas=index.Piñata_idPiñatas,
                                       usuario_cliente_idusuarios=index.usuario_cliente_idusuarios,
                                       Contacto_idContacto=index.Contacto_idContacto)
            model = {'idpedido': Pedi.idpedido, 'Estatus': Pedi.Estatus,
                     'Fecha_Inicio': Pedi.Fecha_Inicio, 'Fecha_Estimada_Final': Pedi.Fecha_Estimada_Final,
                     'Piñata_idPiñatas': Pedi.Piñata_idPiñatas,
                     'usuario_cliente_idusuarios': Pedi.usuario_cliente_idusuarios,
                     'Contacto_idContacto': Pedi.Contacto_idContacto}
            resul.append(model)
        json_resul = json.dumps({'Pedidos': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")

async def get_Pedidos_user_cancel(ID_usuario):
    pin = pedido.select().where(pedido.usuario_cliente_idusuarios == ID_usuario and pedido.Estatus == 'cancelado')
    if pin:
        resul = []
        for index in pin:
            Pedi = PedidoResponseModel(idpedido=index.idpedido,
                                       Estatus=index.Estatus,
                                       Fecha_Inicio=index.Fecha_Inicio,
                                       Fecha_Estimada_Final=index.Fecha_Estimada_Final,
                                       Piñata_idPiñatas=index.Piñata_idPiñatas,
                                       usuario_cliente_idusuarios=index.usuario_cliente_idusuarios,
                                       Contacto_idContacto=index.Contacto_idContacto)
            model = {'idpedido': Pedi.idpedido, 'Estatus': Pedi.Estatus,
                     'Fecha_Inicio': Pedi.Fecha_Inicio, 'Fecha_Estimada_Final': Pedi.Fecha_Estimada_Final,
                     'Piñata_idPiñatas': Pedi.Piñata_idPiñatas,
                     'usuario_cliente_idusuarios': Pedi.usuario_cliente_idusuarios,
                     'Contacto_idContacto': Pedi.Contacto_idContacto}
            resul.append(model)
        json_resul = json.dumps({'Pedidos': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")

async def get_Pedidos():#Muestra todos los pedidos
    pin = pedido.select().order_by(pedido.Estatus.asc()).where((pedido.Estatus == 'pendiente') | (pedido.Estatus == 'listo'))  # aplico un select para obtener toda la informacion
    if pin:
        resul = []
        for index in pin:
            Pedi = PedidoResponseModel(idpedido=index.idpedido,
                                 Estatus=index.Estatus,
                                 Fecha_Inicio=index.Fecha_Inicio,
                                 Fecha_Estimada_Final=index.Fecha_Estimada_Final,
                                 Piñata_idPiñatas=index.Piñata_idPiñatas,
                                 usuario_cliente_idusuarios=index.usuario_cliente_idusuarios,
                                 Contacto_idContacto=index.Contacto_idContacto)
            model = {'idpedido': Pedi.idpedido, 'Estatus': Pedi.Estatus,
                     'Fecha_Inicio': Pedi.Fecha_Inicio, 'Fecha_Estimada_Final': Pedi.Fecha_Estimada_Final,
                     'Piñata_idPiñatas': Pedi.Piñata_idPiñatas, 'usuario_cliente_idusuarios': Pedi.usuario_cliente_idusuarios,
                     'Contacto_idContacto':Pedi.Contacto_idContacto}
            resul.append(model)
        json_resul = json.dumps({'Pedidos': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")

async def Modify_Status(id,req: ModifyStatus):
    ped = pedido.get_or_none(pedido.idpedido == id)
    if ped:
        ped.Estatus = req.Estatus
        ped.save()
        return {"message": f"El estatus se cambio con exito"}
    else:
        raise HTTPException(404,'No se ha encontrado el pedido')
async def get_Pedidos_Finalizado():#Muestra todos los pedidos
    pin = pedido.select().where(pedido.Estatus == 'pagado')  # aplico un select para obtener toda la informacion
    if pin:
        resul = []
        for index in pin:
            Pedi = PedidoResponseModel(idpedido=index.idpedido,
                                 Estatus=index.Estatus,
                                 Fecha_Inicio=index.Fecha_Inicio,
                                 Fecha_Estimada_Final=index.Fecha_Estimada_Final,
                                 Piñata_idPiñatas=index.Piñata_idPiñatas,
                                 usuario_cliente_idusuarios=index.usuario_cliente_idusuarios,
                                 Contacto_idContacto=index.Contacto_idContacto)
            model = {'idpedido': Pedi.idpedido, 'Estatus': Pedi.Estatus,
                     'Fecha_Inicio': Pedi.Fecha_Inicio, 'Fecha_Estimada_Final': Pedi.Fecha_Estimada_Final,
                     'Piñata_idPiñatas': Pedi.Piñata_idPiñatas, 'usuario_cliente_idusuarios': Pedi.usuario_cliente_idusuarios,
                     'Contacto_idContacto':Pedi.Contacto_idContacto}
            resul.append(model)
        json_resul = json.dumps({'Pedidos': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")

async def get_Pedidos_Cancelados():#Muestra todos los pedidos
    pin = pedido.select().where(pedido.Estatus == 'cancelado')  # aplico un select para obtener toda la informacion
    if pin:
        resul = []
        for index in pin:
            Pedi = PedidoResponseModel(idpedido=index.idpedido,
                                 Estatus=index.Estatus,
                                 Fecha_Inicio=index.Fecha_Inicio,
                                 Fecha_Estimada_Final=index.Fecha_Estimada_Final,
                                 Piñata_idPiñatas=index.Piñata_idPiñatas,
                                 usuario_cliente_idusuarios=index.usuario_cliente_idusuarios,
                                 Contacto_idContacto=index.Contacto_idContacto)
            model = {'idpedido': Pedi.idpedido, 'Estatus': Pedi.Estatus,
                     'Fecha_Inicio': Pedi.Fecha_Inicio, 'Fecha_Estimada_Final': Pedi.Fecha_Estimada_Final,
                     'Piñata_idPiñatas': Pedi.Piñata_idPiñatas, 'usuario_cliente_idusuarios': Pedi.usuario_cliente_idusuarios,
                     'Contacto_idContacto':Pedi.Contacto_idContacto}
            resul.append(model)
        json_resul = json.dumps({'Pedidos': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")


async def get_Pedidos_ALL():#Muestra todos los pedidos
    pin = pedido.select().count()  # aplico un select para obtener toda la informacion
    return pin


async def Create_Pedido(Req:PedidoBaseModel):
    res = pedido.select().where(pedido.idpedido == Req.idpedido)
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
    res = pedido.select().where(pedido.idpedido == ID_Pedido and pedido.usuario_cliente_idusuarios == ID_usuario).first()
    if res:
        res.delete_instance()
        return {"message": f"El dato se elimino con éxito"}
    else:
        raise HTTPException(404,"El dato que desea eliminar no existe")
