import json

from MyTables.tipos_de_piñatas import tipos_de_piñatas
from schemas.PinataType import TypeofPinataRequestModel, TypeofPinataResponseModel


async def create_type_pinatas(type_pinata_req: TypeofPinataRequestModel):
    type_pinata_req = tipos_de_piñatas.create(
        idTipos_de_piñatas=type_pinata_req.idTipos_de_piñatas,
        Tipo=type_pinata_req.Tipo
    )
    return type_pinata_req


async def get_typepinata(id_type):
    ty = tipos_de_piñatas.select().where(tipos_de_piñatas.idTipos_de_piñatas == id_type).first()
    if ty:
        return TypeofPinataResponseModel(idTipos_de_piñatas=ty.idTipos_de_piñatas,
                                         Tipo=ty.Tipo)
    else:
        return False


async def get_alltypepinata():
    ty = tipos_de_piñatas.select()
    if ty:
        resul = []
        for index in ty:
            typ = TypeofPinataResponseModel(idTipos_de_piñatas=index.idTipos_de_piñatas,
                                            Tipo=index.Tipo)
            model = {'idTipos_de_piñatas': typ.idTipos_de_piñatas, 'Tipo': typ.Tipo}
            resul.append(model)
        json_resul = json.dumps({'tipos_de_piñatas': resul})
        data = json.loads(json_resul)
        return data
    else:
        return False


async def delete_the_type_pinata(id_type):
    ty = tipos_de_piñatas.select().where(tipos_de_piñatas.idTipos_de_piñatas == id_type).first()
    if ty:
        ty.delete_instance()
    else:
       return False

