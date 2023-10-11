from MyTables.inventario import inventario
from schemas.Inventary import *
from fastapi import HTTPException
import json


async def CreateInvent(Req: InventaryBaseModel):
    res = inventario.select().where(inventario.idInventario == Req.idInventario)
    if res:
        raise HTTPException(404, 'Ya hay un objeto con esa clave')
    else:
        Req = inventario.create(
            idInventario=Req.idInventario,
            Existencia=Req.Existencia,
            Vendido=Req.Vendido,
            Apartado=Req.Apartado,
            Total=Req.Existencia-Req.Vendido-Req.Apartado,
            Piñatas_detalles_idPiñatas_detalles=Req.Piñatas_detalles_idPiñatas_detalles
        )
        return Req


async def GetAllInventory():
    inv = inventario.select()  # aplico un select para obtener toda la informacion
    if inv:
        resul = []
        for index in inv:
            Invent = InventaryResponseModel(idInventario=index.idInventario,
                                        Existencia=index.Existencia,
                                        Vendido=index.Vendido,
                                        Apartado=index.Apartado,
                                        Total=index.Total,
                                        Piñatas_detalles_idPiñatas_detalles=index.Piñatas_detalles_idPiñatas_detalles)
            model = {'idInventario': Invent.idInventario, 'Existencia': Invent.Existencia, 'Vendido': Invent.Vendido,
                     'Apartado': Invent.Apartado,
                     'Total': Invent.Total, 'Piñatas_detalles_idPiñatas_detalles': Invent.Piñatas_detalles_idPiñatas_detalles}
            resul.append(model)
        json_resul = json.dumps({'Inventario': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")


async def Delete_Inventory(ID_Inventory):
    res = inventario.select().where(inventario.idPiñatas == ID_Inventory)
    if res:
        res.delete_instance()
    else:
        raise HTTPException(404,"El dato que desea eliminar no existe")

async def Modify_Inventory(ID_Inventory,Req:InventaryDataModel):
    xor = inventario.get_or_none(inventario.idInventario == ID_Inventory)
    if xor:
        if Req.Existencia != None:
            xor.Existencia = Req.Existencia
        if Req.Vendido != 0:
            xor.Vendido = Req.Vendido
        if Req.Apartado != 0:
            xor.Apartado = Req.Apartado
        Val = int(xor.Existencia)-int(Req.Vendido)-int(Req.Apartado)
        xor.Total = Val
        xor.save()
        return {"message": f"El dato ya fue modificado con exito"}
    else:
        raise HTTPException(404,"El objeto que anda buscando no existe")