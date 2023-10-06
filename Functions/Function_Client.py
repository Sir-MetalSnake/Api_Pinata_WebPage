from MyTables.usuario_cliente import usuario_cliente
from schemas.usuarioclient import UserClientRequestModel,UserClient_Modify_Pass

from fastapi import HTTPException # REQUEST EXCEPTION

#Class Client


async def create_user(user_req: UserClientRequestModel):
    res = usuario_cliente.select().where(usuario_cliente.usuario == user_req.usuario)
    if res:
        return HTTPException(404,'This User is already exist')
    else:
        user_req = usuario_cliente.create(
            usuario=user_req.usuario,
            contraseña=user_req.contraseña,
            Correo=user_req.Correo
        )
        return user_req


async def get_user(id_usuarios):
    user = usuario_cliente.select().where(usuario_cliente.idusuarios == id_usuarios)
    if user:
        return True
    else:
        return False


async def get_userandpass(usuario, password):
    user = usuario_cliente.select().where(usuario_cliente.usuario == usuario and usuario_cliente.contraseña == password)
    if user:
        return True
    else:
        return False


async def deleteuser(id_usuarios):
    user = usuario_cliente.select().where(usuario_cliente.idusuarios == id_usuarios).first()
    if user:
        user.delete_instance()
        return True
    else:
        return False


async def Modify_User(id_usuario, usuario_request: UserClientRequestModel):
    user = usuario_cliente.select().where(usuario_cliente.idusuarios == id_usuario).first()
    if user:
        for index, item in usuario_request:
            setattr(user, index, item)

        user.save()
        return True
    else:
        return HTTPException(404, 'Client not found')


async def Modify_Password(usuario, usuario_req: UserClient_Modify_Pass):
    res = usuario_cliente.get_or_none(usuario_cliente.usuario == usuario)
    if res:
        res.contraseña = usuario_req.contraseña
        res.save()
        return {"message": f"La Contraseña a sido actualizada"}
    else:
        return HTTPException(404, 'Client not found')