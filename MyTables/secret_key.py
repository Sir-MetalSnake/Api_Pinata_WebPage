from database import *
from usuario_cliente import usuario_cliente
class secret_key(Model):
    idKey = IntegerField(primary_key=True)
    KeyName = TextField(primary_key=False)
    Id_usuario = IntegerField(ForeignKeyField(usuario_cliente, field= "idusuarios", column_name='Id_usuario'))
    Fecha_de_exp = DateTimeField(primary_key=False)

    def __str__(self):
        return self.KeyName

    class Meta:
        database = database
        table_name = 'secret_key'
