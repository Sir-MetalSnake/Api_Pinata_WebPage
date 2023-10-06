from database import *


class tipos_de_piñatas(Model):
    idTipos_de_piñatas = IntegerField(primary_key=True)
    Nombre_festividad = CharField(max_length=45)

    def __int__(self):
        return self.idTipos_de_piñatas

    class Meta:
        database = database
        table_name = 'tipos_de_piñatas'
