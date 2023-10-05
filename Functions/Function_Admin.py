from MyTables.usuario_admin import usuario_admin
from schemas.useradmin import UserAdminRequestModel
from fastapi import HTTPException # REQUEST EXCEPTION

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
        return True
    else:
        raise HTTPException(404, 'Admin not found')
