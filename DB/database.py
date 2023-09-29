from peewee import *

# oap2

database = MySQLDatabase(
    'pinatas_fantasy',
    user='root',
    password='Ruiz181002', host='localhost', port=3306
)


class usuario_cliente(Model):
    idusuarios = IntegerField
    usuario = CharField(max_length=50)
    contraseña = CharField(max_length=100)
    correo = CharField(max_length=50)
    def __str__(self):
        return self.idusuarios

    class Meta:
        database = database
