from MyTables.tipos_de_piñatas import tipos_de_piñatas
from schemas.PinataType import TypeofPinataRequestModel, TypeofPinataResponseModel


async def create_type_pinatas(type_pinata_req: TypeofPinataRequestModel):
    type_pinata_req = tipos_de_piñatas.create(
        idTipos_de_piñatas=type_pinata_req.idTipos_de_piñatas,
        Tipo=type_pinata_req.Tipo
    )
    return type_pinata_req


async def get_typepinata(id_type):
    ty = tipos_de_piñatas.select().where(tipos_de_piñatas.idTipos_de_piñatas == id_type)
    if ty:
        return TypeofPinataResponseModel(idTipos_de_piñatas=ty.idTipos_de_piñatas,
                                         Tipo=ty.Tipo)
    else:
        return False