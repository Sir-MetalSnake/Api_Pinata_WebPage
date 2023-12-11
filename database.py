import os
from peewee import *
from dotenv import load_dotenv
# oap2
load_dotenv()
DB_NAME = str(os.getenv('DB_NAME'))
USER = str(os.getenv('DB_USER'))
PASSWD = str(os.getenv('DB_PASSW'))
HOST = str(os.getenv('DB_HOST'))
PORT = int(os.getenv('DB_PORT'))
database = MySQLDatabase(
    DB_NAME,
    user=USER, password=PASSWD,
    host=HOST, port=PORT
)