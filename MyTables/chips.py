from database import *

class chips(Model):
    Id_Chip = IntegerField(primary_key=True)
    Detail = CharField(50)

    def __str__(self):
        return self.Detail

    class Meta:
        database = database
        table_name = 'chips'
