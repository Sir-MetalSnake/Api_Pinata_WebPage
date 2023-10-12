from MyTables.piñata import piñata
from MyTables.usuario_cliente import usuario_cliente
from MyTables.Contacto import Contacto
from database import *


class pedido(Model):
    idpedido = IntegerField(primary_key=True)
    Estatus = CharField(max_length=45)
    Fecha_Inicio = CharField(max_length=45)
    Fecha_Estimada_Final = CharField(max_length=45)
    Piñata_idPiñatas = IntegerField(ForeignKeyField(piñata, field="idPiñatas", backref='pedido', column_name='Piñata_idPiñatas'))
    usuario_cliente_idusuarios = IntegerField(ForeignKeyField(usuario_cliente, field="idusuarios", backref='pedido', column_name='usuario_cliente_idusuarios'))
    Contacto_idContacto = IntegerField(ForeignKeyField(Contacto, field="idContacto", backref='pedido', column_name='Contacto_idContacto'))

    def __int__(self):
        return self.idpedido

    class Meta:
        database = database
        table_name = 'pedido'