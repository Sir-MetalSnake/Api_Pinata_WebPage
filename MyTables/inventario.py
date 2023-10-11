from MyTables.Piñatas_detalles import piñatas_detalles
from database import *

class inventario(Model):
    idInventario = IntegerField(primary_key=True)
    Existencia = IntegerField(primary_key=False)
    Vendido = IntegerField(primary_key=False)
    Apartado = IntegerField(primary_key=False)
    Total = IntegerField(primary_key=False)
    Piñatas_detalles_idPiñatas_detalles = IntegerField(ForeignKeyField(piñatas_detalles, field= "idPiñatas_detalles",
                                                          backref='inventario', column_name='Piñatas_detalles_idPiñatas_detalles'))

    def __int__(self):
        return self.idInventario

    class Meta:
        database = database
        table_name = 'inventario'
