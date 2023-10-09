from database import *


class Contacto(Model):
    idContacto = IntegerField(primary_key=True)
    Direccion = CharField(max_length=45)
    Telefono = CharField(max_length=10)

    def __int__(self):
        return self.idContacto

    class Meta:
        database = database
        table_name = 'Contacto'
