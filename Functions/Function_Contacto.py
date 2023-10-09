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