from MyTables.usuario_cliente import usuario_cliente
from schemas.usuarioclient import *
import jwt
from jwt import PyJWTError
from fastapi import HTTPException,Depends # REQUEST EXCEPTION
import logging
from datetime import *
logging.basicConfig(level=logging.DEBUG)
#Class Client
SECRET_KEY = "OPTIMISTAPRIME"
ALGORITHM = "HS512"
ACCESS_TOKEN_EXPIRE_MINUTES = 5


async def login_user(request_login):
    user = request_login.username
    password = request_login.password
    token = await authenticate_user(user, password)
    return {'access_token': token, 'token_type': 'bearer'}


async def authenticate_user(user: str, password: str):
    Usuario = usuario_cliente.get_or_none(usuario_cliente.usuario == user and usuario_cliente.contraseña == password)

    if Usuario is None or not usuario_cliente.contraseña == password:
        raise HTTPException(status_code=404, detail='Worker not found or incorrect password')

    access_token_expires = timedelta(hours=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token_data = {
        "sub": Usuario.usuario,
        "exp": datetime.utcnow() + access_token_expires,
    }
    access_token = jwt.encode(access_token_data, SECRET_KEY, algorithm=ALGORITHM)

    return access_token
async def get_current_user(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user = usuario_cliente.get(usuario_cliente.usuario == username)
    except PyJWTError:
        raise HTTPException(status_code=401, detail="No autorizado")
    return user

async def Verify_Token_User(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        User= usuario_cliente.get_or_none(usuario_cliente.usuario == username)
        if User:
            return {"message": f"El usuario es User"}
        else:
            raise HTTPException(401, "No es un Usuario")
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Token expirado o invalido")


async def create_user(user_req: UserClientRequestModel):
    res = usuario_cliente.select().where(usuario_cliente.usuario == user_req.usuario)
    if res:
        return HTTPException(404,'This User is already exist')
    else:
        user_req = usuario_cliente.create(
            usuario=user_req.usuario,
            contraseña=user_req.contraseña,
            Correo=user_req.Correo,
            Nombre=user_req.Nombre,
            Apellido_P=user_req.Apellido_P,
            Apellido_M=user_req.Apellido_M,
            Telefono=user_req.Telefono
        )
        return user_req


async def get_user(id_usuarios):
    user = usuario_cliente.get_or_none(usuario_cliente.idusuarios == id_usuarios | usuario_cliente.usuario == id_usuarios)
    if user:
        return UserClientResponseModel(idusuarios=user.idusuarios,
                                       usuario=user.usuario,
                                       Correo=user.Correo,
                                       contraseña=user.contraseña,
                                       Nombre=user.Nombre,
                                       Apellido_P=user.Apellido_P,
                                       Apellido_M=user.Apellido_M,
                                       Telefono=user.Telefono)
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
    user = usuario_cliente.get_or_none(usuario_cliente.idusuarios == id_usuario)
    if user:
        user.usuario = usuario_request.usuario if usuario_request.usuario is not None else user.usuario
        user.contraseña = usuario_request.contraseña if usuario_request.contraseña is not None else user.contraseña
        user.Correo = usuario_request.Correo if usuario_request.Correo is not None else user.Correo
        user.Nombre = usuario_request.Nombre if usuario_request.Nombre is not None else user.Nombre
        user.Apellido_P = usuario_request.Apellido_P if usuario_request.Apellido_P is not None else user.Apellido_P
        user.Apellido_M = usuario_request.Apellido_M if usuario_request.Apellido_M is not None else user.Apellido_M
        user.Telefono = usuario_request.Telefono if usuario_request.Telefono is not None else user.Telefono
        user.save()
        return {"message": f"Se ha modificado la información con exito"}
    else:
        return HTTPException(404, 'Client not found')


async def Modify_Password(usuario, usuario_req: UserClient_Modify_Pass):
    res = usuario_cliente.get_or_none(usuario_cliente.usuario == usuario)
    if res:
        res.contraseña = usuario_req.contraseña
        res.save()
        return {"message": f"La Contraseña a sido actualizada"}
    else:
        raise HTTPException(404, 'Client not found')

async def Modify_Tel(usuario, usuario_request: UserClient_Modify_Tel):
    res = usuario_cliente.get_or_none(usuario_cliente.usuario == usuario)
    if res:
        res.Telefono = usuario_request.Telefono
        res.save()
        return {"message": f"El telefono a sido actualizado"}
    else:
        raise HTTPException(404, 'Client not found')