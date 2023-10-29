from database import *
from MyTables.piñata import piñata
class colors(Model):
    id_color = IntegerField(primary_key=True)
    Name = CharField(50)
    Imagen = CharField(50)
    Id_Piñatas = IntegerField(ForeignKeyField(piñata, field="idPiñatas", column_name="Id_Piñatas"))

    def __str__(self):
        return self.Name

    class Meta:
        database = database
        table_name = 'colors'