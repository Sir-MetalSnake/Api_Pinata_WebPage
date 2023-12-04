from MyTables.piñata import piñata
from database import *

class inventario(Model):
    idInventario = IntegerField(primary_key=True)
    disponibilidad = IntegerField(primary_key=False)
    Existencia = IntegerField(primary_key=False)
    Vendido = IntegerField(primary_key=False)
    Apartado = IntegerField(primary_key=False)
    Total = IntegerField(primary_key=False)
    id_Piñatas_inv = IntegerField(ForeignKeyField(piñata, field= "idPiñatas",
                                                          backref='inventario', column_name='id_Piñatas_inv'))

    def __int__(self):
        return self.idInventario

    class Meta:
        database = database
        table_name = 'inventario'
