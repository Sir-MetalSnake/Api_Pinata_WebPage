import os.path
import uuid

from fastapi import FastAPI, HTTPException, Depends, UploadFile,File
from fastapi.responses import FileResponse
from database import database as connection
from fastapi.middleware.cors import CORSMiddleware
#Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#My Schemas of my Data Base
from schemas.Contact import *
from schemas.Favorite import *
from schemas.Inventary import *
from schemas.PinataType import *
from schemas.ProcesoDelPedido import *
from schemas.Tags_Chips import *
from schemas.fetividad import *
from schemas.pinata import *
from schemas.usuarioclient import *
from schemas.useradmin import *
from schemas.Pinta_detail import *
from schemas.Pedido_Schema import *
from schemas.Colors_model import *
# mis bibliotecas

from Functions import Function_Client as Client
from Functions import Function_Pinatas_Type as Typep
from Functions import Function_Admin as Admin
from Functions import Function_festividades as Fest
from Functions import Function_Contacto as Conct
from Functions import Function_Pinata as Pinata
from Functions import Function_Pinata_detail as Detail
from Functions import Function_Inventario as Invent
from Functions import Function_Pedido as Pedid
from Functions import Function_ProcesoPedido as procesoP
from Functions import Function_favorite as favoriteU
from Functions import Aditionals as Add
from Functions import Function_Chips as Tag
from Functions import Function_Colors as Col

app = FastAPI(title='My API',
              description='Esta es mi API',
              version=' 1.0.1')


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
app.add_middleware(CORSMiddleware,
                    allow_origins=["*"],
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"])

oauth2_scheme_user = OAuth2PasswordBearer(tokenUrl="Loginprueba",scheme_name="oauth2_User")
oauth2_scheme_Admin = OAuth2PasswordBearer(tokenUrl="LoginAdmin",scheme_name="oauth2_Admin")
ROUTE = 'img_pinatas/'
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        allowFile= {"image/jpeg", "image/jpg", "image/png", "image/gif"}
        if file.content_type in allowFile:
            file_extension = file.filename.split('.')[-1]
            file.filename = f"{uuid.uuid4()}.{file_extension}"
            contents = file.file.read()
            with open(f"{ROUTE}{file.filename}", 'wb') as f:
                f.write(contents)
        else:
            raise HTTPException(404, 'Tipo de archivo incorrecto')
    except Exception:
        raise HTTPException(404, 'Error al momento de subir el archivo')
    finally:
        file.file.close()
    return {"message": f"{file.filename}"}

@app.get("/show")
async def read_file(rout):
    path = f"{ROUTE}{rout}"
    return FileResponse(path)

@app.delete("/delete_file")
async def delete(rout):
    path = f"{ROUTE}{rout}"
    if os.path.exists(path):
        os.remove(path)
        return {"Message": f"Imagen eliminada con éxito"}
    else:
        raise HTTPException(404,'File not found')
#auth


@app.post('/Loginprueba', tags=['Usuario'])
async def login(request_login: OAuth2PasswordRequestForm = Depends()):
    return await Client.login_user(request_login)

@app.get('/user/me', tags=['Usuario'])
async def get_current_user(token: str = Depends(oauth2_scheme_user)):
    return await Client.get_current_user(token)


@app.get('/Check_Token_User', tags=['Usuario'])
async def Check(token: str = Depends(oauth2_scheme_user)):
    return await Client.Verify_Token_User(token)


@app.post('/LoginAdmin', tags=['Admin'])#Logeo con el admin
async def loginAdmin(request_login2: OAuth2PasswordRequestForm = Depends()):
    return await Admin.login_userAdmin(request_login2)


@app.get('/userAdmin/me', tags=['Admin'])
async def get_current_user(token2: str = Depends(oauth2_scheme_Admin)):
    return await Admin.get_current_userAdmin(token2)


@app.get('/Check_Token_Admin', tags=['Admin'])
async  def Check(token: str = Depends(oauth2_scheme_Admin)):
    return await Admin.Verify_Token_Admin(token)

# Function


@app.get('/hol', tags=['Usuario'])
async def hol(request_login: str = Depends(oauth2_scheme_user)):
    return "hola funciona"
# Client API


@app.post('/Send_Mail', tags=["Usuario"])
async def Send_Mail_Code_Verify(user):
    return await Add.Send_Mail_Code_Verify(user)

@app.post('/Comprobar', tags=["Usuario"])
async def Compare_Secret_Key(Key):
    return await Add.Compare_Secret_Key(Key)


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
    return await Client.Modify_User(id_usuario, usuario_request)


@app.patch('/usuario_cliente/{usuario}', tags=["Usuario"])
async def Modify_Password(usuario, usuario_req: UserClient_Modify_Pass):
    return await Client.Modify_Password(usuario, usuario_req)

@app.patch('/Modificar_telefono/{usuario}', tags=["Usuario"])
async def Modify_Tel(usuario, usuario_req: UserClient_Modify_Pass):
    return await Client.Modify_Tel(usuario, usuario_req)


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


@app.patch('/usuario_admin/', tags=["Admin"])
async def Modify_Password_Admin(newPass: Modify_Admin_Password, token: str = Depends(oauth2_scheme_Admin)):
    return await Admin.Modify_Password_Admin(token, newPass)

# type of pinata
@app.post('/tipos_de_piñatas', tags=["type of pinata"])
async def create_type_pinata(TypePinata_req: TypeofPinataRequestModel):
    return await Typep.create_type_pinatas(TypePinata_req)


@app.get('/tipos_de_piñatas/{id_type}', tags=["type of pinata"])
async def get_typepinata(id_type):
    return await Typep.get_typepinata(id_type)


@app.get('/Get_ALL_tipos_de_piñatas', tags=["type of pinata"])
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

#regionpiñata
@app.get('/piñata_PerOrder/{Orden}', tags=["Piñata"])
async def GetAll_InOrder(Orden):
    return await Pinata.GetAll_InOrder(Orden)

@app.get('/piñata_PerPrice/{Price}', tags=["Piñata"])
async def GetAll_InMinNumber(Price):
    return await Pinata.GetAll_InMinNumber(Price)

@app.get('/piñata/{dato}', tags=["Piñata"])
async def GetAll_PinataSearch(dato):
    return await Pinata.GetAll_PinataSearch(dato)


@app.get('/piñata', tags=["Piñata"])
async def GetAll_Pinata():
    return await Pinata.GetAll_Pinata()

@app.get('/GetPinata/{id}',tags=["Piñata"])
async def GetPinataWithID(id):
    return await Pinata.GetPinataWithID(id)

@app.patch('/piñata', tags=["Piñata"])
async def Modify_Piñata(ID_Pinata,Req:ModifyPinata):
    return await Pinata.Modify_Piñata(ID_Pinata,Req)


@app.post('/piñata', tags=["Piñata"])
async def Create_Pinata(Req:PinataBASEMODEL):
    return await Pinata.Create_Pinata(Req)


@app.delete('/piñata/{ID_Pinata}', tags=["Piñata"])
async def Delete_Pinata(ID_Pinata):
    return await Pinata.Delete_Pinata(ID_Pinata)
#endregion

#Pinata Details
@app.get('/piñatas_detalles/{ID_Pinata}', tags=["Piñata_detalles"])
async def Get_PinataDetail(ID_Pinata):
    return await Detail.Get_Pinata_detail(ID_Pinata)


@app.post('/piñatas_detalles', tags=["Piñata_detalles"])
async def Create_PinataDetail(Req:Pinata_detailBASEMODEL):
    return await Detail.Create_PinataDetail(Req)


@app.delete('/piñatas_detalles/{ID_Pinata}', tags=["Piñata_detalles"])
async def Delete_PinataDetail(ID_Pinata):
    return await Detail.Delete_PinataDetail(ID_Pinata)

@app.patch('/piñatas_detalles', tags=["Piñata_detalles"])
async def Modify_Piñata_detail(ID_Pinata,Req:ModifyPinata_detail):
    return await Detail.Modify_Piñata_detail(ID_Pinata, Req)

#Inventario


@app.get('/inventario', tags=["Inventario"])
async def GetAll_Inventory():
    return await Invent.GetAllInventory()


@app.get('/Check_inventario', tags=["Inventario"])
async def CheckInventory(idPinata):
    return await Invent.CheckInventory(idPinata)

@app.get('/Get_Inventory_pinata',tags=['Inventario'])
async def GetInventarioPerIdPinata(idpinata):
    return await Invent.GetInventarioPerIdPinata(idpinata)

@app.get('/inventoryperdata/{data}', tags=["Inventario"])
async def GetAllInventoryperData(data):
    return await Invent.GetAllInventoryperData(data)


@app.post('/inventario', tags=["Inventario"])
async def Create_Invent(Req: InventaryBaseModel):
    return await Invent.CreateInvent(Req)


@app.delete('/inventario/{ID_Inventory}', tags=["Inventario"])
async def Delete_Inventory(ID_Inventory):
    return await Invent.Delete_Inventory(ID_Inventory)


@app.patch('/inventario/{ID_Inventory}', tags=["Inventario"])
async def Modify_Inventory(ID_Inventory,Req:InventaryDataModel):
    return await Invent.Modify_Inventory(ID_Inventory, Req)


@app.patch('/discontinue',tags=["Inventario"])
async def discontinue_Inventory(ID_Inv, Req:InventoryState):
    return await Invent.discontinue_Inventory(ID_Inv, Req)

# Pedido
@app.post('/pedido', tags=["Pedido"])
async def Create_Pedido(Req:PedidoBaseModel):
    return await Pedid.Create_Pedido(Req)

@app.get('/pedido/{ID_usuario}', tags=["Pedido"])
async def get_Pedidos_user(ID_usuario):
    return await Pedid.get_Pedidos_user(ID_usuario)

@app.get('/pedido_user_fin/{ID_usuario}', tags=["Pedido"])
async def get_Pedidos_user_finalizado(ID_usuario):
    return await Pedid.get_Pedidos_user_finalizado(ID_usuario)

@app.get('/pedido_user_Notf/{ID_usuario}', tags=["Pedido"])
async def get_Pedidos_user_notify(ID_usuario):
    return await Pedid.get_Pedidos_user_notify(ID_usuario)


@app.get('/GetPedidos_user_Cancel/{ID_usuario}',tags=['Pedido'])
async def get_Pedidos_user_cancel(ID_usuario):
    return await Pedid.get_Pedidos_user_cancel(ID_usuario)

@app.get('/getallpedido', tags=["Pedido"])
async def get_Pedidos_ALL():
    return await Pedid.get_Pedidos_ALL()

@app.get('/getallpedido_cancelados', tags=["Pedido"])
async def get_Pedidos_Cancelados():
    return await Pedid.get_Pedidos_Cancelados()

@app.get('/pedido', tags=["Pedido"])
async def get_Pedidos():
    return await Pedid.get_Pedidos()

@app.get('/GetAllPedidos_Fin', tags=['Pedido'])
async def get_Pedidos_Finalizado():
    return await Pedid.get_Pedidos_Finalizado()

@app.patch('/Modify_Pedido', tags=['Pedido'])
async def Modify_Status(id, req:ModifyStatus):
    return await Pedid.Modify_Status(id, req)

@app.delete('/pedido/{ID_Pedido}/{ID_usuario}', tags=["Pedido"])
async def Delete_Pedido(ID_Pedido,ID_usuario):
    return await Pedid.Delete_Pedido(ID_Pedido, ID_usuario)

#Proceso del pedido

@app.post('/proceso_del_pedido', tags=["Proceso_Del_Pedido"])
async def Create_Procedo_Del_Pedido(Req: ProcesoPedidoRequestModel):
    return await procesoP.Create_Procedo_Del_Pedido(Req)

@app.get('/proceso_del_pedido/{ID}', tags=["Proceso_Del_Pedido"])
async def get_Proceso_Del_Pedido(ID):
    return await procesoP.get_Proceso_Del_Pedido(ID)


@app.patch('/Mod_proceso', tags=["Proceso_Del_Pedido"])
async def Modify_Anticipo_Final(ID, req:PagoFinalModify):
    return await procesoP.Modify_Anticipo_Final(ID, req)


@app.get('/favoritos/{Id_usuario}', tags=["favoritos"])
async def GetFavoritos(Id_usuario):
    return await favoriteU.GetFavoritos(Id_usuario)
@app.post('/favoritos', tags=["favoritos"])
async def CreateFavoritos(Req: FavoriteBaseModel):
    return await favoriteU.CreateFavoritos(Req)

@app.delete('/favoritos/{id_usuario}/{id_favorito}', tags=["favoritos"])
async def Delete_Favoritos(id_usuario,id_favorito):
    return await favoriteU.Delete_Favoritos(id_usuario,id_favorito)

@app.get('/Get_All_Chips',tags=['Etiqueta'])
async def Get_All_Tags():
    return await Tag.Get_All_Tags()

@app.get('/Get_Tag',tags=['Etiqueta'])
async def Get_chip(id):
    return await Tag.Get_chip(id)

@app.post('/Add_Tag',tags=['Etiqueta'])
async def Create_Tag(TagReq:Model_Chip):
    return await Tag.Create_Tag(TagReq)

@app.delete('/Delete_tag',tags=['Etiqueta'])
async def Delete_Tag(idTag):
    return await Tag.Delete_Tag(idTag)

@app.put('/Modify_Tag', tags=['Etiqueta'])
async def Modify_Tag(idTag, tag_req: Model_Chip):
    return await Tag.Modify_Tag(idTag, tag_req)


@app.get('/Get_color_pinata', tags=['Colors'])
async def Get_All_Color(id_pinata):
    return await Col.Get_All_Color(id_pinata)

@app.get('/Get_ALL_Colors',tags=['Colors'])
async def Get_All_Colors():
    return await Col.Get_All_Colors()

@app.post('/Add_color_pinata', tags=['Colors'])
async def Create_Color(Color_Req:Colors_Main_Model):
    return await Col.Create_Color(Color_Req)


@app.put('/Modify_color_Pinata', tags=['Colors'])
async def Modify_Color(idColor, color_req: Colors_Main_Model):
    return await Col.Modify_Color(idColor,color_req)


@app.delete('/Delete_color_Pinata', tags=['Colors'])
async def Delete_Color(idColor):
    return await Col.Delete_Color(idColor)
#Agregar etiquetas de colores, personajes(filtros)
#agregar tabla de ships (id_chip, id_pinata)
#tabla (id_color,nombre_color, id_pinata)