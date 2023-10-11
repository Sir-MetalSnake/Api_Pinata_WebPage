from MyTables.Piñatas_detalles import piñatas_detalles
from schemas.Pinta_detail import *
from fastapi import HTTPException
import json


async def GetAll_Pinata_detail():
    pin = piñatas_detalles.select()  # aplico un select para obtener toda la informacion
    if pin:
        resul = []
        for index in pin:
            pinat = MyID_DetailResponse(idPiñatas_detalles=index.idPiñatas_detalles,
                               Tamaño=index.Tamaño,
                               Colores=index.Colores,
                               Tiempo_estimado=index.Tiempo_estimado,
                               Stock=index.Stock,
                               Piñata_idPiñatas=index.Piñata_idPiñatas)
            model = {'idPiñatas_detalles': pinat.idPiñatas_detalles, 'Tamaño': pinat.Tamaño,'Colores': pinat.Colores,'Tiempo_estimado': pinat.Tiempo_estimado,
                     'Stock': pinat.Stock,'Piñata_idPiñatas': pinat.Piñata_idPiñatas}
            resul.append(model)
        json_resul = json.dumps({'piñatas_detalles': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404,"No tiene ningun campo agregado")


async def Get_Pinata_detail(ID_Pinata):
    res = piñatas_detalles.select().where(piñatas_detalles.Piñata_idPiñatas == ID_Pinata).first()
    if res:
        return MyID_DetailResponse(idPiñatas_detalles=res.idPiñatas_detalles,
                                   Tamaño=res.Tamaño,
                                   Colores=res.Colores,
                                   Tiempo_estimado=res.Tiempo_estimado,
                                   Stock=res.Stock,
                                   Piñata_idPiñatas=res.Piñata_idPiñatas)
    else:
        raise HTTPException(404,"No se ha encontrado el dato")


async def Modify_Piñata_detail(ID_Pinata,Req:ModifyPinata_detail):
    xor = piñatas_detalles.get_or_none(piñatas_detalles.idPiñatas_detalles == ID_Pinata)
    if xor:
        xor.Tamaño = Req.Tamaño
        xor.Colores = Req.Colores
        xor.Tiempo_estimado = Req.Tiempo_estimado
        xor.Stock = Req.Stock
        xor.Piñata_idPiñatas = Req.Piñata_idPiñatas
        xor.save()
        return {"message": f"El dato ya fue modificado con exito"}
    else:
        raise HTTPException(404,"El objeto que anda buscando no existe")


async def Create_PinataDetail(Req:Pinata_detailBASEMODEL):
    res = piñatas_detalles.select().where(piñatas_detalles.idPiñatas_detalles == Req.idPiñatas_detalles)
    if res:
        raise HTTPException(404, 'Ya hay un objeto con esa clave')
    else:
        Req = piñatas_detalles.create(
            idPiñatas_detalles=Req.idPiñatas_detalles,
            Tamaño=Req.Tamaño,
            Colores=Req.Colores,
            Tiempo_estimado=Req.Tiempo_estimado,
            Stock=Req.Stock,
            Piñata_idPiñatas=Req.Piñata_idPiñatas
        )
        return Req


async def Delete_PinataDetail(ID_Pinata):
    res = piñatas_detalles.select().where(piñatas_detalles.idPiñatas_detalles == ID_Pinata).first()
    if res:
        res.delete_instance()
        return {"message": f"El dato ya fue Eliminado con exito"}
    else:
        raise HTTPException(404,"El dato que desea eliminar no existe")