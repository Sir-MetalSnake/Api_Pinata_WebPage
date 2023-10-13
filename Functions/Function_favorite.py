import json

from MyTables.favoritos import favoritos
from schemas.Favorite import *
from fastapi import HTTPException

async def CreateFavoritos(Req: FavoriteBaseModel):
    res=favoritos.select().where(favoritos.id_piñata == Req.id_piñata)
    if res:
        raise HTTPException(404, 'Ya tiene dentro de favoritos ese producto')
    else:
        Req= favoritos.create(
            id_piñata=Req.id_piñata,
            id_user=Req.id_user)
        return Req


async def GetFavoritos(Id_usuario):
    Fav = favoritos.select().where(favoritos.id_user == Id_usuario)  # aplico un select para obtener toda la informacion
    if Fav:
        resul = []
        for index in Fav:
            Favorit = FavoriteModelResponse(id_Favorito=index.id_Favorito,
                                         id_piñata=index.id_piñata,
                                         id_user=index.id_user)
            model = {'id_Favorito': Favorit.id_Favorito, 'id_piñata': Favorit.id_piñata,
                     'id_user': Favorit.id_user}
            resul.append(model)
        json_resul = json.dumps({'Favoritos': resul})
        data = json.loads(json_resul)
        return data
    else:
        raise HTTPException(404, "No tiene ningun campo agregado")



async def Delete_Favoritos(id_usuario, id_favorito):
    res = favoritos.select().where(favoritos.id_user == id_usuario and favoritos.id_Favorito == id_favorito).first()
    if res:
        res.delete_instance()
        return True
    else:
        raise HTTPException(404, "El favorito que desea eliminar no existe")



