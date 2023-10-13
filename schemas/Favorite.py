from pydantic import BaseModel


class FavoriteBaseModel(BaseModel):
    id_piñata: int
    id_user: int

class FavoriteModelResponse(FavoriteBaseModel):
    id_Favorito: int