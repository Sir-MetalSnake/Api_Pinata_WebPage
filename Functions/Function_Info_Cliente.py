from MyTables.Info_cliente import Info_cliente
from schemas.Infocliente import *
from fastapi import HTTPException # REQUEST EXCEPTION


async def get_Info_cliente(id_usuario):
    Info = Info_cliente.select().where(Info_cliente.usuario_cliente_idusuarios == id_usuario).first()
    if Info:
        print(Info.id_info_cliente,Info.Nombre, Info.Apellido_P, Info.Apellido_M, Info.Telefono, Info.usuario_cliente_idusuarios)
        return InfoClienteResponse(id_info_cliente=Info.id_info_cliente,
                                   Nombre=Info.Nombre,
                                   Apellido_P=Info.Apellido_P,
                                   Apellido_M=Info.Apellido_M,
                                   Telefono=Info.Telefono,
                                   usuario_cliente_idusuarios=Info.usuario_cliente_idusuarios)
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