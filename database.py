from peewee import *

# oap2

database = MySQLDatabase(
    'pinatas_fantasy',
    user='root', password='Ruiz181002',
    host='localhost', port=3306
)




# Parte del Admin

class usuario_admin(Model):
    idusuario_admin = IntegerField(primary_key=True)
    usuario = CharField(max_length=45)
    contraseña = CharField(max_length=45)

    def __str__(self):
        return self.usuario

    class Meta:
        database = database
        table_name = 'usuario_admin'