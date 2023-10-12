from MyTables.Info_cliente import Info_cliente
from schemas.Infocliente import *
from fastapi import HTTPException # REQUEST EXCEPTION

async def get_Info_cliente(id_usuario):
    Inflo_cliente = Info_cliente.select().where(Info_cliente.usuario_cliente_idusuarios == id_usuario)
    if Inflo_cliente:
        return InfoClienteResponse(Nombre=Inflo_cliente.Nombre,
                                   Apellido_P=Inflo_cliente.Apellido_P,
                                   Apellido_M=Inflo_cliente.Apellido_M,
                                   Telefono=Inflo_cliente.Telefono,
                                   usuario_cliente_idusuarios=Inflo_cliente.usuario_cliente_idusuarios)
    else:
        raise HTTPException(404, "No se ha encontrado el dato")



async def Modify_User(id_info_cliente, usuario_request: InfoClient_Modify_Tel):
    res = Info_cliente.get_or_none(Info_cliente.id_info_cliente == id_info_cliente)
    if res:
        res.tel = usuario_request.telefono
        res.save()
        return {"message": f"El telefono a sido actualizado"}
    else:
        raise HTTPException(404, 'Client not found')



async def Create_Info_User(Req: InfoClientRequestModel):
    res = Info_cliente.select().where(Info_cliente.usuario_cliente_idusuarios == Req.usuario_cliente_idusuarios)
    if res:
        raise HTTPException(404, 'Ya hay un objeto con esa clave')
    else:
        Req = Info_cliente.create(
            Nombre=Req.Nombre,
            Apellido_P=Req.Apellido_P,
            Apellido_M=Req.Apellido_M,
            telefono=Req.telefono,
            usuario_cliente_idusuarios=Req.usuario_cliente_idusuarios
        )
        return Req

async def Delete_Info_User(ID_Info):
    res = Info_cliente.select().where(Info_cliente.id_info_cliente == ID_Info)
    if res:
        res.delete_instance()
        return True
    else:
        raise HTTPException(404,"El dato que desea eliminar no existe")