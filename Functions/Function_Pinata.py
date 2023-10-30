from MyTables.piñata import *
from schemas.pinata import *
from fastapi import HTTPException
import json


async def GetAll_Pinata():
    pin = piñata.select()  # aplico un select para obtener toda la informacion
    if pin:
        resul = []
        for index in pin:
            pinat = MyIDResponse(idPiñatas=index.idPiñatas,
                                 Nombre_pinata=index.Nombre_pinata,
                                 idTipos_de_piñatas=index.idTipos_de_piñatas,
                                 idFestividades=index.idFestividades,
                                 Precio=index.Precio,
                                 Imagen=index.Imagen,
                                 Id_Tag=index.Id_Tag)
            model = {'idPiñatas': pinat.idPiñatas, 'Nombre_pinata': pinat.Nombre_pinata,
                     'idTipos_de_piñatas': pinat.idTipos_de_piñatas, 'idFestividades': pinat.idFestividades,
                     'Precio': pinat.Precio, 'Imagen': pinat.Imagen, 'Id_Tag': pinat.Id_Tag}
            resul.append(model)
        json_resul = json.dumps({'piñata': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")


async def GetAll_PinataSearch(dato):
    pin = piñata.select().where(
        piñata.Nombre_pinata.contains(dato))  # aplico un select para obtener toda la informacion
    if pin:
        resul = []
        for index in pin:
            pinat = MyIDResponse(idPiñatas=index.idPiñatas,
                                 Nombre_pinata=index.Nombre_pinata,
                                 idTipos_de_piñatas=index.idTipos_de_piñatas,
                                 idFestividades=index.idFestividades,
                                 Precio=index.Precio,
                                 Imagen=index.Imagen,
                                 d_Tag=index.Id_Tag)
            model = {'idPiñatas': pinat.idPiñatas, 'Nombre_pinata': pinat.Nombre_pinata,
                     'idTipos_de_piñatas': pinat.idTipos_de_piñatas, 'idFestividades': pinat.idFestividades,
                     'Precio': pinat.Precio, 'Imagen': pinat.Imagen, 'Id_Tag': pinat.Id_Tag}
            resul.append(model)
        json_resul = json.dumps({'piñata': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")


async def Modify_Piñata(ID_Pinata, Req: ModifyPinata):
    xor = piñata.get_or_none(piñata.idPiñatas == ID_Pinata)
    if xor:
        xor.Nombre_pinata = Req.Nombre_pinata if Req.Nombre_pinata is not None else xor.Nombre_pinata
        xor.idTipos_de_piñatas = Req.idTipos_de_piñatas if Req.idTipos_de_piñatas is not None else xor.idTipos_de_piñatas
        xor.idFestividades = Req.idFestividades if Req.idFestividades is not None else xor.idFestividades
        xor.Precio = Req.Precio if Req.Precio is not None else xor.Precio
        xor.Imagen = Req.Imagen if Req.Imagen is not None else xor.Imagen
        xor.Id_Tag = Req.Id_Tag if Req.Id_Tag is not None else xor.Id_Tag
        xor.save()
        return {"message": f"El dato ya fue modificado con exito"}
    else:
        raise HTTPException(404, "El objeto que anda buscando no existe")


async def Create_Pinata(Req: PinataBASEMODEL):
    res = piñata.select().where(piñata.idPiñatas == Req.idPiñatas).first()
    if res:
        raise HTTPException(404, 'Ya hay un objeto con esa clave')
    else:
        Req = piñata.create(
            idPiñatas=Req.idPiñatas,
            Nombre_pinata=Req.Nombre_pinata,
            idTipos_de_piñatas=Req.idTipos_de_piñatas,
            idFestividades=Req.idFestividades,
            Precio=Req.Precio,
            Imagen=Req.Imagen,
            Id_Tag=Req.Id_Tag
        )
        return Req


async def Delete_Pinata(ID_Pinata):
    res = piñata.select().where(piñata.idPiñatas == ID_Pinata).first()
    if res:
        res.delete_instance()
        return {"message": f"El dato se elimino con éxito"}
    else:
        raise HTTPException(404, "El dato que desea eliminar no existe")
