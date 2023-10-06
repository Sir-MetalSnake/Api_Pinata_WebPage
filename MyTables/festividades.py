from database import *

class festividades(Model):
    idFestividades = IntegerField(primary_key=True)
    Tipo = CharField(max_length=45)

    def __int__(self):
        return self.idFestividades

    class Meta:
        database = database
        table_name = 'festividades'