from database import *
class usuario_cliente(Model):
    idusuarios = IntegerField(primary_key=True)
    usuario = CharField(max_length=45)
    contraseña = TextField(primary_key=False)
    Correo = CharField(max_length=50)
    Nombre = CharField(max_length=50)
    Apellido_P = CharField(max_length=50)
    Apellido_M = CharField(max_length=50)
    Telefono = CharField(max_length=10)
    def __str__(self):
        return self.usuario

    class Meta:
        database = database
        table_name = 'usuario_cliente'
