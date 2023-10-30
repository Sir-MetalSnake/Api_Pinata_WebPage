from database import *
from MyTables.piñata import *

class piñatas_detalles(Model):
    idPiñatas_detalles = IntegerField(primary_key=True)
    Tamaño = CharField(max_length=45)
    Tiempo_estimado = CharField(max_length=45)
    Stock = IntegerField(primary_key=False)
    Piñata_idPiñatas = IntegerField(ForeignKeyField(piñata, field= "idPiñatas", backref='piñatas_detalles', column_name='Piñata_idPiñatas'))

    def __int__(self):
        return self.idPiñatas_detalles

    class Meta:
        database = database
        table_name = 'piñatas_detalles'
