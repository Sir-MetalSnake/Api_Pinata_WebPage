from database import *


class favoritos(Model):
    id_Favorito = IntegerField(primary_key=True)
    id_piñata = IntegerField(primary_key=False)
    id_user = IntegerField(primary_key=False)

    def __int__(self):
        return self.id_Favorito

    class Meta:
        database = database
        table_name = 'favoritos'
