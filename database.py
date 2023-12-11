import os
from peewee import *
from dotenv import load_dotenv
# oap2
load_dotenv()

database = MySQLDatabase(
    'pinatas_fantasy',
    user='root', password='EAb562bDEBfAGAgAHG3dHB32fdcCH6B4',
    host='roundhouse.proxy.rlwy.net', port=40116
)