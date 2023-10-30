from database import *
from MyTables.chips import chips
from MyTables.tipos_de_piñatas import tipos_de_piñatas
from MyTables.festividades import festividades


class piñata(Model):
    idPiñatas = IntegerField(primary_key=True)
    Nombre_pinata = CharField(max_length=45)
    idTipos_de_piñatas = IntegerField(ForeignKeyField(tipos_de_piñatas
                                                      , field='idTipos_de_piñatas'
                                                      , column_name='idTipos_de_piñatas'))
    idFestividades = IntegerField(ForeignKeyField(festividades, field='idFestividades'
                                                  , column_name='idFestividades'))
    Precio = FloatField(primary_key=False)
    Imagen = CharField(max_length=200)
    Id_Tag = IntegerField(ForeignKeyField(chips, field='Id_Chip', column_name='Id_Tag'))

    def __int__(self):
        return self.idPiñatas

    class Meta:
        database = database
        table_name = 'piñata'
