from MyTables.Contacto import *
from schemas.Contact import *
from fastapi import HTTPException # REQUEST EXCEPTION


async def get_Contact(id_Contact):
    Ct = Contacto.select().where(Contacto.idContacto == id_Contact).first()
    if Ct:
        return ContactResponse(idContacto=Ct.idContacto,
                                Direccion=Ct.Direccion,
                               Telefono= Ct.Telefono)
    else:
        raise HTTPException(404,"El dato que desea buscar no existe")


async def create_Contact(Req: ContactBaseModel):
    res = Contacto.select().where(Contacto.idContacto == Req.idContacto)
    if res:
        raise HTTPException(404, 'Ya hay un objeto con esa llave')
    else:
        Req = Contacto.create(
            idFestividades=Req.idContacto,
            Direccion=Req.Direccion,
            Telefono=Req.Telefono
        )
        return Req