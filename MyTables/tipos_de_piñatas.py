from database import  *


class tipos_de_piñatas(Model):
    idTipos_de_piñatas = IntegerField(primary_key=True)
    Tipo = CharField(max_length=45)

    def __str__(self):
        return self.Tipo

    class Meta:
        database = database
        table_name = 'tipos_de_piñatas'
