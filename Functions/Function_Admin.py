from MyTables.usuario_admin import usuario_admin
from schemas.useradmin import UserAdminRequestModel


async def createadmin(useradmin_request: UserAdminRequestModel):
    user = usuario_admin.create(
        usuario=useradmin_request.usuario,
        contraseña=useradmin_request.contraseña
    )
    return useradmin_request