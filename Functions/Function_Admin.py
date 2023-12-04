from MyTables.usuario_admin import usuario_admin
from schemas.useradmin import UserAdminRequestModel,Modify_Admin_Password
from fastapi import HTTPException # REQUEST EXCEPTION
import jwt
from jwt import PyJWTError
from fastapi import HTTPException,Depends,Request # REQUEST EXCEPTION
import logging
from datetime import *
logging.basicConfig(level=logging.DEBUG)
#Class Admin
SECRET_KEY = "OPTIMISTAPRIME"
ALGORITHM = "HS512"
ACCESS_TOKEN_EXPIRE_MINUTES = 5

#Auth User Admin
async def login_userAdmin(request_login):
    user = request_login.username
    password = request_login.password
    token = await authenticate_userAdmin(user, password)
    return {'access_token': token, 'token_type': 'bearer'}

async def authenticate_userAdmin(user: str, password: str):
    Usuario = usuario_admin.get_or_none(usuario_admin.usuario == user and usuario_admin.contraseña == password)

    if Usuario is None or not usuario_admin.contraseña == password:
        raise HTTPException(status_code=404, detail='Usuario incorrecto')

    access_token_expires = timedelta(hours=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token_data = {
        "sub": Usuario.usuario,
        "exp": datetime.utcnow() + access_token_expires,
    }
    access_token = jwt.encode(access_token_data, SECRET_KEY, algorithm=ALGORITHM)

    return access_token
async def get_current_userAdmin(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user = usuario_admin.get(usuario_admin.usuario == username)
    except PyJWTError:
        raise HTTPException(status_code=401, detail="No autorizado")
    return user

async def Verify_Token_Admin(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        User = usuario_admin.get_or_none(usuario_admin.usuario == username)
        if User:
            return {"message": f"El usuario es Admin"}
        else:
            raise HTTPException(401,"No es un Admin")
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Token expirado o invalido")

async def createadmin(useradmin_request: UserAdminRequestModel):
    useradmin_request = usuario_admin.create(
        usuario=useradmin_request.usuario,
        contraseña=useradmin_request.contraseña
    )
    return useradmin_request


async def get_useradminandpass(usuario, password):
    user = usuario_admin.select().where(usuario_admin.usuario == usuario and usuario_admin.contraseña == password)
    if user:
        return True
    else:
        return False


async def Modify_UserAdmin(id_usuario, admin_request: UserAdminRequestModel):
    user = usuario_admin.select().where(usuario_admin.idusuario_admin == id_usuario).first()
    if user:
        for index, item in admin_request:
            setattr(user, index, item)

        user.save()
        return {"message": f"Se ha modificado la información con exito"}
    else:
        raise HTTPException(404, 'Admin not found')

async def Modify_Password_Admin(token, newPass: Modify_Admin_Password):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario: str = payload.get("sub")
        res = usuario_admin.get_or_none(usuario_admin.usuario == usuario)
        if res:
            res.contraseña = newPass.contraseña
            res.save()
            return {"message": f"La Contraseña a sido actualizada"}
    except PyJWTError:
        raise HTTPException(status_code=401, detail="No autorizado")