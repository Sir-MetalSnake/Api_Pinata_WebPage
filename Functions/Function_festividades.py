from MyTables.festividades import festividades
from schemas.fetividad import FestividadBaseModel, FestividadResponse
from fastapi import HTTPException # REQUEST EXCEPTION
import json


async def create_Festivity(Festivity_req: FestividadBaseModel):
    res = festividades.select().where(festividades.idFestividades == Festivity_req.idFestividades)
    if res:
        raise HTTPException(404, 'Ya hay un objeto con esa llave')
    else:
        Festivity_req = festividades.create(
            idFestividades=Festivity_req.idFestividades,
            Nombre_festividad=Festivity_req.Nombre_festividad
        )
        return Festivity_req


async def get_Festivity(id_Festivity):
    ty = festividades.select().where(festividades.idFestividades == id_Festivity).first()
    if ty:
        return FestividadResponse(idFestividades=ty.idFestividades,
                                         Nombre_festividad=ty.Nombre_festividad)
    else:
        return False



async def get_allFestivity():
    ty = festividades.select()
    if ty:
        resul = []
        for index in ty:
            typ = FestividadResponse(idFestividades=index.idFestividades,
                                            Nombre_festividad=index.Nombre_festividad)
            model = {'idFestividades': typ.idFestividades, 'Nombre_festividad': typ.Nombre_festividad}
            resul.append(model)
        json_resul = json.dumps({'festividades': resul})
        data = json.loads(json_resul)
        return data
    else:
        return False


async def delete_Festivity(id_Festivity):
    ty = festividades.select().where(festividades.idFestividades == id_Festivity).first()
    if ty:
        ty.delete_instance()
        return True
    else:
       return False

