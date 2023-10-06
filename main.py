from fastapi import FastAPI, HTTPException
from database import database as connection
from MyTables.usuario_admin import usuario_admin
from MyTables.usuario_cliente import usuario_cliente
from schemas.PinataType import TypeofPinataRequestModel
from schemas.usuarioclient import (UserClientRequestModel, UserClient_Modify_Pass,
                                   UserClientResponseModel)
from schemas.useradmin import UserAdminRequestModel

# mis bibliotecas

from Functions import Function_Client as Client
from Functions import Function_Pinatas_Type as Typep
from Functions import Function_Admin as Admin

app = FastAPI(title='My API',
              description='Esta es mi API',
              version=' 1.0.1')


# Function


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Client API

@app.get('/usuario_cliente/{id_usuarios}')
async def get_user(id_usuarios):
    return await Client.get_user(id_usuarios)


@app.get('/usuario_cliente/{usuario}/{password}')
async def get_userandpass(usuario, password):
    return await Client.get_userandpass(usuario, password)


@app.post("/usuario_cliente")
async def create_user(user_req: UserClientRequestModel):
    return await Client.create_user(user_req)


@app.put('/usuario_cliente/{id_usuario}')
async def Modify_User(id_usuario, usuario_request: UserClientRequestModel):
    return Client.Modify_User(id_usuario, usuario_request)


@app.patch('/usuario_cliente/{usuario}')
async def Modify_Password(usuario, usuario_req: UserClient_Modify_Pass):
    return await Client.Modify_Password(usuario, usuario_req)


@app.delete('/usuario_cliente/{id_usuarios}')
async def deleteuser(id_usuarios):
    return await Client.deleteuser(id_usuarios)


# administrador

@app.post("/usuario_admin")
async def createadmin(useradmin_request: UserAdminRequestModel):
    return await Admin.createadmin(useradmin_request)


@app.get('/usuario_admin/{usuario}/{password}')
async def get_useradminandpass(usuario, password):
    return await Admin.get_useradminandpass(usuario, password)


@app.put('/usuario_admin/{id_usuario}')
async def Modify_UserAdmin(id_usuario, admin_request: UserAdminRequestModel):
    return await Admin.Modify_UserAdmin(id_usuario, admin_request)


# type of pinata
@app.post('/tipos_de_piñatas')
async def create_type_pinata(TypePinata_req: TypeofPinataRequestModel):
    return await Typep.create_type_pinatas(TypePinata_req)


@app.get('/tipos_de_piñatas/{id_type}')
async def get_typepinata(id_type):
    return await Typep.get_typepinata(id_type)


@app.get('/tipos_de_piñatas')
async def get_all_TypeP():
    return await Typep.get_alltypepinata()


@app.delete('/tipos_de_piñatas/{id_type}')
async def delete_the_type_pinata(id_type):
    return await Typep.delete_the_type_pinata(id_type)

# Festividades

