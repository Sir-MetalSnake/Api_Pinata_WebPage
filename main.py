from fastapi import FastAPI, HTTPException
from database import database as connection

#My Schemas of my Data Base
from schemas.Contact import *
from schemas.Inventary import *
from schemas.PinataType import *
from schemas.fetividad import *
from schemas.pinata import *
from schemas.usuarioclient import *
from schemas.useradmin import *
from schemas.Pinta_detail import *
# mis bibliotecas

from Functions import Function_Client as Client
from Functions import Function_Pinatas_Type as Typep
from Functions import Function_Admin as Admin
from Functions import Function_festividades as Fest
from Functions import Function_Contacto as Conct
from Functions import Function_Pinata as Pinata
from Functions import Function_Pinata_detail as detail
from Functions import Function_Inventario as Invent
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


@app.get('/piñata', tags=["Piñata"])
async def GetAll_Pinata():
    return await Pinata.GetAll_Pinata()


@app.patch('/piñata/{ID_Pinata}', tags=["Piñata"])
async def Modify_Piñata(ID_Pinata,Req:ModifyPinata):
    return await Pinata.Modify_Piñata(ID_Pinata,Req)


@app.post('/piñata', tags=["Piñata"])
async def Create_Pinata(Req:PinataBASEMODEL):
    return await Pinata.Create_Pinata(Req)


@app.delete('/piñata/{ID_Pinata}', tags=["Piñata"])
async def Delete_Pinata(ID_Pinata):
    return await Pinata.Delete_Pinata(ID_Pinata)

#Pinata Details


@app.get('/piñatas_detalles/{ID_Pinata}', tags=["Piñata_detalles"])
async def Get_PinataDetail(ID_Pinata):
    return await detail.Get_Pinata_detail(ID_Pinata)


@app.post('/piñatas_detalles', tags=["Piñata_detalles"])
async def Create_PinataDetail(Req:Pinata_detailBASEMODEL):
    return await detail.Create_PinataDetail(Req)


@app.delete('/piñatas_detalles/{ID_Pinata}', tags=["Piñata_detalles"])
async def Delete_PinataDetail(ID_Pinata):
    return await detail.Delete_PinataDetail(ID_Pinata)

@app.patch('/piñatas_detalles', tags=["Piñata_detalles"])
async def Modify_Piñata_detail(ID_Pinata,Req:ModifyPinata_detail):
    return await detail.Modify_Piñata_detail(ID_Pinata, Req)

#Inventario


@app.get('/inventario', tags=["Inventario"])
async def GetAll_Inventory():
    return await Invent.GetAllInventory()


@app.post('/inventario', tags=["Inventario"])
async def Create_Invent(Req: InventaryBaseModel):
    return await Invent.CreateInvent(Req)


@app.delete('/inventario/{ID_Inventory}', tags=["Inventario"])
async def Delete_Inventory(ID_Inventory):
    return await Invent.Delete_Inventory(ID_Inventory)

@app.patch('/inventario/{ID_Inventory}', tags=["Inventario"])
async def Modify_Inventory(ID_Inventory,Req:InventaryDataModel):
    return await Invent.Modify_Inventory(ID_Inventory, Req)