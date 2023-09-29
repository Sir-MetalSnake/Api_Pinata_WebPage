from fastapi import FastAPI

from DB.database import database as connection

app = FastAPI(title='My API',
              description='Esta es mi API',
              version=' 1.0.1')


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/usuario_cliente")
async def create_user():
    return 'cliente'
