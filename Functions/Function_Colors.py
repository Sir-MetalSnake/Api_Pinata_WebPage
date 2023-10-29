from MyTables.colors import colors
from schemas.Colors_model import *
import json
from fastapi import HTTPException


async def Get_All_Color(id_pinata):
    color = colors.select().where(colors.Id_Piñatas == id_pinata)
    if color:
        resul = []
        for index in color:
            Col = Colors_Response(Id_color=index.Id_color, Name=index.Name, Imagen=index.Imagen, Id_Piñatas=index.Id_Piñatas)
            model = {'Id_color': Col.Id_color, 'Name': Col.Name, 'Imagen': Col.Imagen, 'Id_Piñatas': Col.Id_Piñatas}
            resul.append(model)
        json_resul = json.dumps({'Colores': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404,'No tiene agregado un color de acuerdo a esa piñata')


async def Create_Color(Color_Req:Colors_Main_Model):
    Color_Req = colors.create(
        Name=Color_Req.Name,
        Imagen=Color_Req.Imagen,
        Id_Piñatas=Color_Req.Id_Piñatas
    )
    return Color_Req


async def Modify_Color(idColor, color_req: Colors_Main_Model):
    Col = colors.get_or_none(colors.id_color == idColor)
    if Col:

        Col.Name = color_req.Name if color_req.Name is not None else Col.Name
        Col.Imagen = color_req.Imagen if color_req.Imagen is not None else Col.Imagen
        Col.Id_Piñatas = color_req.Id_Piñatas if color_req.Id_Piñatas is not None else Col.Id_Piñatas
        Col.save()
        return {"message": f"Se ha modificado la información con exito"}
    else:
        return HTTPException(404, 'Tag not found')


async def Delete_Color(idColor):
    Tg = colors.select().where(colors.id_color == idColor).first()
    if Tg:
        Tg.delete_instance()
        return {"message": f"El color se elimino con éxito"}
    else:
        raise HTTPException(404, "El color que desea eliminar no existe")
