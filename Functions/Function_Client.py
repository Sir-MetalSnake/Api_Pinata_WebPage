from MyTables.usuario_cliente import usuario_cliente
from schemas.usuarioclient import UserClientRequestModel

from fastapi import HTTPException # REQUEST EXCEPTION

#Class Client


async def create_user(user_req: UserClientRequestModel):
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