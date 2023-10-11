from database import *

from database import *
class Info_cliente(Model):
    id_info_cliente = IntegerField(primary_key=True)
    Nombre = CharField(max_length=45)
    Apellido_P = CharField(max_length=45)
    Apellido_M = CharField(max_length=45)
    Telefono = CharField(max_length=45)
    def __str__(self):
        return self.Nombre

    class Meta:
        database = database
        table_name = 'Info_cliente'
