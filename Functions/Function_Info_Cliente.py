from MyTables import Info_cliente



async def get_Info_cliente(id_info_cliente):
    Inflo_cliente = Info_cliente.select().where(Info_cliente.id_info_cliente == id_info_cliente)
    if Inflo_cliente:
        return True
    else:
        return False