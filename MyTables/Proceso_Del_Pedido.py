from database import *

class proceso_del_pedido(Model):
    ID = IntegerField(primary_key=True)
    pedido_idpedido = IntegerField(primary_key=False)
    Anticipo = CharField(max_length=45)
    Pago_Final = CharField(max_length=45)

    def __int__(self):
        return self.pedido_idpedido

    class Meta:
        database = database
        table_name = 'proceso_del_pedido'