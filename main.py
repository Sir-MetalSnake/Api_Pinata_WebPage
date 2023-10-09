from fastapi import FastAPI, HTTPException
from database import database as connection
from schemas.Contact import *
from schemas.PinataType import TypeofPinataRequestModel
from schemas.fetividad import *
from schemas.usuarioclient import *
from schemas.useradmin import *

# mis bibliotecas

from Functions import Function_Client as Client
from Functions import Function_Pinatas_Type as Typep
from Functions import Function_Admin as Admin
from Functions import Function_festividades as Fest
from Functions import Function_Contacto as Conct

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
@app.get('/usuario_cliente/{id_usuarios}', tags=["Usuario"])
async def get_user(id_usuarios):
    return await Client.get_user(id_usuarios)


@app.get('/usuario_cliente/{usuario}/{password}', tags=["Usuario"])
async def get_userandpass(usuario, password):
    return await Client.get_userandpass(usuario, password)


@app.post("/usuario_cliente", tags=["Usuario"])
async def create_user(user_req: UserClientRequestModel):
    return await Client.create_user(user_req)


@app.put('/usuario_cliente/{id_usuario}', tags=["Usuario"])
async def Modify_User(id_usuario, usuario_request: UserClientRequestModel):
    return Client.Modify_User(id_usuario, usuario_request)


@app.patch('/usuario_cliente/{usuario}', tags=["Usuario"])
async def Modify_Password(usuario, usuario_req: UserClient_Modify_Pass):
    return await Client.Modify_Password(usuario, usuario_req)


@app.delete('/usuario_cliente/{id_usuarios}', tags=["Usuario"])
async def deleteuser(id_usuarios):
    return await Client.deleteuser(id_usuarios)


# administrador

@app.post("/usuario_admin", tags=["Admin"])
async def createadmin(useradmin_request: UserAdminRequestModel):
    return await Admin.createadmin(useradmin_request)


@app.get('/usuario_admin/{usuario}/{password}', tags=["Admin"])
async def get_useradminandpass(usuario, password):
    return await Admin.get_useradminandpass(usuario, password)


@app.put('/usuario_admin/{id_usuario}', tags=["Admin"])
async def Modify_UserAdmin(id_usuario, admin_request: UserAdminRequestModel):
    return await Admin.Modify_UserAdmin(id_usuario, admin_request)


@app.patch('/usuario_admin/{usuario}', tags=["Admin"])
async def Modify_Password_Admin(usuario, newPass: Modify_Admin_Password):
    return await Admin.Modify_Password_Admin(usuario, newPass)


# type of pinata
@app.post('/tipos_de_piñatas', tags=["type of pinata"])
async def create_type_pinata(TypePinata_req: TypeofPinataRequestModel):
    return await Typep.create_type_pinatas(TypePinata_req)


@app.get('/tipos_de_piñatas/{id_type}', tags=["type of pinata"])
async def get_typepinata(id_type):
    return await Typep.get_typepinata(id_type)


@app.get('/tipos_de_piñatas', tags=["type of pinata"])
async def get_all_TypeP():
    return await Typep.get_alltypepinata()


@app.delete('/tipos_de_piñatas/{id_type}', tags=["type of pinata"])
async def delete_the_type_pinata(id_type):
    return await Typep.delete_the_type_pinata(id_type)

# Festividades

@app.post('/festividades', tags=["festividades"])
async def create_Festivity(Festivity_req: FestividadBaseModel):
    return await Fest.create_Festivity(Festivity_req)


@app.get('/festividades/{id_Festivity}', tags=["festividades"])
async def get_Festivity(id_Festivity):
    return await Fest.get_Festivity(id_Festivity)


@app.get('/festividades', tags=["festividades"])
async def get_allFestivity():
    return await Fest.get_allFestivity()


@app.delete('/festividades/{id_Festivity}', tags=["festividades"])
async def delete_Festivity(id_Festivity):
    return await Fest.delete_Festivity(id_Festivity)


#contacto
@app.get('/Contacto/{id_Contact}', tags=["Contacto"])
async def get_Contact(id_Contact):
    return await Conct.get_Contact(id_Contact)


@app.post('/Contacto', tags=["Contacto"])
async def create_Contact(Req: ContactBaseModel):
    return await Conct.create_Contact(Req)


@app.patch('/Contacto/{id_Contact}', tags=["Contacto"])
async def Modify_Contacto(id_Contact, req: ContactEditBase):
    return await Conct.Modify_Contacto(id_Contact,req)


@app.delete('/Contacto/{id_Contact}', tags=["Contacto"])
async def Delete_Contacto(id_Contact):
    return await Conct.Delete_Contacto(id_Contact)

#piñata
