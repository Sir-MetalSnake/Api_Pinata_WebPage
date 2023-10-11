from MyTables.Piñatas_detalles import piñatas_detalles
from database import *

class inventario(Model):
    idInventario = IntegerField(primary_key=True)
    Existencia = int
    Vendido = int
    Apartado = int
    Total = int
    Piñatas_detalles_idPiñatas_detalles = ForeignKeyField(piñatas_detalles, field= "idPiñatas_detalles",
                                                          backref='inventario', column_name='Piñatas_detalles_idPiñatas_detalles')

    def __int__(self):
        return self.idInventario

    class Meta:
        database = database
        table_name = 'inventario'
