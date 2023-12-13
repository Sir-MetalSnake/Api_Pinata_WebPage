from MyTables.inventario import inventario
from MyTables.piñata import piñata
from MyTables.Piñatas_detalles import piñatas_detalles
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
            disponibilidad=Req.disponibilidad,
            Existencia=Req.Existencia,
            Vendido=Req.Vendido,
            Apartado=Req.Apartado,
            Total=Req.Existencia-Req.Vendido-Req.Apartado,
            id_Piñatas_inv=Req.id_Piñatas_inv
        )
        return Req

async def CheckInventory(idPinata):
    inv = inventario.select().where((inventario.id_Piñatas_inv == idPinata) &
                                    (inventario.disponibilidad == 1)).first()
    if inv:
        return True
    else:
        return False

async def GetInventarioPerIdPinata(idPinata):
    inv = inventario.select().where(inventario.id_Piñatas_inv == idPinata).first()

    if inv:
        return InventaryResponseModel(idInventario=inv.idInventario,
                                        disponibilidad=inv.disponibilidad,
                                        Existencia=inv.Existencia,
                                        Vendido=inv.Vendido,
                                        Apartado=inv.Apartado,
                                        Total=inv.Total,
                                        id_Piñatas_inv=inv.id_Piñatas_inv)

    else:
        raise HTTPException(404, "No tiene ningun campo agregado")

async def GetAllInventory():
    inv = inventario.select().order_by(inventario.disponibilidad.desc())  # aplico un select para obtener toda la informacion
    if inv:
        resul = []
        for index in inv:
            Invent = InventaryResponseModel(idInventario=index.idInventario,
                                        disponibilidad=index.disponibilidad,
                                        Existencia=index.Existencia,
                                        Vendido=index.Vendido,
                                        Apartado=index.Apartado,
                                        Total=index.Total,
                                        id_Piñatas_inv=index.id_Piñatas_inv)
            model = {'idInventario': Invent.idInventario,'disponibilidad': Invent.disponibilidad,
                     'Existencia': Invent.Existencia, 'Vendido': Invent.Vendido,
                     'Apartado': Invent.Apartado,
                     'Total': Invent.Total, 'id_Piñatas_inv': Invent.id_Piñatas_inv}
            resul.append(model)
        json_resul = json.dumps({'Inventario': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")

async def GetAllInventoryperData(Data):
    inv = (inventario.select().join(piñata, on=(inventario.id_Piñatas_inv == piñata.idPiñatas))
           .where((piñata.Nombre_pinata.contains(Data)) | (inventario.idInventario == Data)))  # aplico un select para obtener toda la informacion
    if inv:
        resul = []
        for index in inv:
            Invent = InventaryResponseModel(idInventario=index.idInventario,
                                            disponibilidad=index.disponibilidad,
                                            Existencia=index.Existencia,
                                            Vendido=index.Vendido,
                                            Apartado=index.Apartado,
                                            Total=index.Total,
                                            id_Piñatas_inv=index.id_Piñatas_inv)
            model = {'idInventario': Invent.idInventario, 'disponibilidad': Invent.disponibilidad,
                     'Existencia': Invent.Existencia, 'Vendido': Invent.Vendido,
                     'Apartado': Invent.Apartado,
                     'Total': Invent.Total, 'id_Piñatas_inv': Invent.id_Piñatas_inv}
            resul.append(model)
        json_resul = json.dumps({'Inventario': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")

async def Delete_Inventory(ID_Inventory):
    res = inventario.select().where(inventario.idInventario == ID_Inventory).first()
    if res:
        res.delete_instance()
        return {"message": f"Se elimino el dato con éxito"}
    else:
        raise HTTPException(404,"El dato que desea eliminar no existe")


async def discontinue_Inventory(ID_Inv, Req:InventoryState):
    xor = inventario.get_or_none(inventario.idInventario == ID_Inv)
    if xor:
        xor.disponibilidad = Req.disponibilidad
        xor.save()
        return {"message": f"El dato ya fue modificado con exito"}
    else:
        raise HTTPException(404, "El objeto que anda buscando no existe")

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
        return xor
    else:
        raise HTTPException(404,"El objeto que anda buscando no existe")