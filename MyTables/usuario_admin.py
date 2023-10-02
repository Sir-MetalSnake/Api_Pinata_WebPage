from database import *


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