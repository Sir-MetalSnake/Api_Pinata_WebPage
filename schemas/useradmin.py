from pydantic import BaseModel


class UserAdminRequestModel(BaseModel):
    usuario: str
    contraseña: str


class Modify_Admin_Password(BaseModel):
    contraseña: str


class UserAdminResponseModel(UserAdminRequestModel):
    idusuario_admin: int
