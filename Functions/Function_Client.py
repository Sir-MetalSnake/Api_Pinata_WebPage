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