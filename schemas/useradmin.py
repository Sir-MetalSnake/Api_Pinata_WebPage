from pydantic import BaseModel


class UserAdminRequestModel(BaseModel):
    usuario: str
    contraseña: str


class UserAdminResponseModel(UserAdminRequestModel):
    idusuario_admin: int
