from MyTables.chips import chips
from schemas.Tags_Chips import *
import json
from fastapi import HTTPException


async def Get_All_Tags():
    ch = chips.select()
    if ch:
        resul = []
        for index in ch:
            chip = Model_ChipResponse(Id_Chip=index.Id_Chip,
                                     Detail=index.Detail)
            model = {'Id_Chip': chip.Id_Chip, 'Detail': chip.Detail}
            resul.append(model)
        json_resul = json.dumps({'Etiquetas': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404,'No tiene agregado alguna etiqueta')

async def Get_chip(id):
    ch = chips.get_or_none(chips.Id_Chip == id)
    if ch:
        return Model_ChipResponse(Id_Chip=ch.Id_Chip,Detail=ch.Detail)
    else:
        raise HTTPException(404,'Etiqueta no encontrada')


async def Create_Tag(TagReq:Model_Chip):
    res = chips.select().where(chips.Id_Chip == TagReq.Id_Chip)
    if res:
        return HTTPException(404, 'This Tag is already exist')
    else:
        TagReq = chips.create(
            Id_Chip=TagReq.Id_Chip,
            Detail=TagReq.Detail
        )
        return TagReq


async def Modify_Tag(idTag,tag_req: Model_Chip):
    tg = chips.get_or_none(idTag == chips.Id_Chip)
    if tg:
        tg.Id_Chip = tag_req.Id_Chip if tag_req.Id_Chip is not None else tg.Id_Chip
        tg.Detail = tag_req.Detail if tag_req.Detail is not None else tg.Detail
        tg.save()
        return {"message": f"Se ha modificado la información con exito"}
    else:
        return HTTPException(404, 'Tag not found')

async def Delete_Tag(idTag):
    Tg = chips.select().where(chips.Id_Chip == idTag).first()
    if Tg:
        Tg.delete_instance()
        return {"message": f"Etiqueta eliminada con éxito"}
    else:
        raise HTTPException(404, "La etiqueta que desea eliminar no existe")
