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
            idContacto=Req.idContacto,
            Direccion=Req.Direccion,
            Telefono=Req.Telefono
        )
        return Req


async def Modify_Contacto(id_Contact, req: ContactEditBase):
    res = Contacto.get_or_none(Contacto.idContacto == id_Contact)
    if res:
        res.Direccion = req.Direccion
        res.Telefono = req.Telefono
        res.save()
        return {"message": f"Los datos han sido actualizados"}
    else:
        raise HTTPException(404, 'No se ha encontrado el dato')


async def Delete_Contacto(id_Contact):
    Con = Contacto.select().where(Contacto.idContacto == id_Contact).first()
    if Con:
        Con.delete_instance()
        return {"message": f"El dato ya fue eliminado con exito"}
    else:
        return HTTPException(404, 'No se ha encontrado el dato')