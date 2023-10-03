from fastapi import FastAPI, HTTPException
from database import database as connection
from MyTables.usuario_admin import usuario_admin
from MyTables.usuario_cliente import usuario_cliente
from schemas.usuarioclient import UserClientRequestModel, UserClientResponseModel
from schemas.useradmin import UserAdminRequestModel

#mis bibliotecas

from Functions import Function_Client as Client

app = FastAPI(title='My API',
              description='Esta es mi API',
              version=' 1.0.1')

#Function



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

#Client API


@app.post("/usuario_cliente")
async def create_user(user_req: UserClientRequestModel):
    return await Client.create_user(user_req)


#
@app.get('/usuario_cliente/{id_usuarios}')
async def get_user(id_usuarios):
    user = usuario_cliente.select().where(usuario_cliente.idusuarios == id_usuarios)
    if user:
        return True
    else:
        return False


@app.get('/usuario_cliente/{usuario}/{password}')
async def get_userandpass(usuario, password):
    user = usuario_cliente.select().where(usuario_cliente.usuario == usuario and usuario_cliente.contraseña == password)
    if user:
        return True
    else:
        return False

@app.delete('/usuario_cliente/{id_usuarios}')
async def deleteuser(id_usuarios):
    user = usuario_cliente.select().where(usuario_cliente.idusuarios == id_usuarios).first()
    if user:
        user.delete_instance()
        return True
    else:
        return False


@app.put('/usuario_cliente/{id_usuario}')
async def Modify_User(id_usuario, usuario_request: UserClientRequestModel):
    user = usuario_cliente.select().where(usuario_cliente.idusuarios == id_usuario).first()
    if user:
        for index, item in usuario_request:
            setattr(user, index, item)

        user.save()
        return True
    else:
        return HTTPException(404, 'Client not found')

@app.post("/usuario_admin")
async def createadmin(useradmin_request:UserAdminRequestModel):
    user = usuario_admin.create(
        usuario=useradmin_request.usuario,
        contraseña=useradmin_request.contraseña
    )
    return useradmin_request


@app.get('/usuario_admin/{usuario}/{password}')
async def get_useradminandpass(usuario, password):
    user = usuario_admin.select().where(usuario_admin.usuario == usuario and usuario_admin.contraseña == password)
    if user:
        return True
    else:
        return False


@app.put('/usuario_admin/{id_usuario}')
async def Modify_UserAdmin(id_usuario, admin_request: UserAdminRequestModel):
    user = usuario_admin.select().where(usuario_admin.idusuario_admin == id_usuario).first()
    if user:
        for index, item in admin_request:
            setattr(user, index, item)

        user.save()
        return True
    else:
        return HTTPException(404, 'Admin not found')
