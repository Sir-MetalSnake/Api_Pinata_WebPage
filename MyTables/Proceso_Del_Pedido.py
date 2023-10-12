from database import *

class ProcesoPedido(Model):
    ID = IntegerField(primary_key=True)
    pedido_idpedido = IntegerField
    Anticipo = CharField(max_length=45)
    Pago_Final = CharField(max_length=45)

    class Meta:
        database = database
        table_name = 'poceso_del_pedido'