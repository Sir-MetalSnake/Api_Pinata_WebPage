from database import *


class piñata(Model):
    idPiñatas = IntegerField(primary_key=True)
    Nombre_pinata = CharField(max_length=45)
    idTipos_de_piñatas = IntegerField(primary_key=False)
    idFestividades = IntegerField(primary_key=False)
    Precio = FloatField(primary_key=False)
    Imagen = CharField(max_length=200)

    def __int__(self):
        return self.idPiñatas

    class Meta:
        database = database
        table_name = 'piñata'
