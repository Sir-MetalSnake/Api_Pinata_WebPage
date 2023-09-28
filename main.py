from fastapi import FastAPI

app = FastAPI(title='My API',
              description='Esta es mi API',
              version='1.0.1')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
