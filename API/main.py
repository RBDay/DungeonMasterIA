from fastapi import FastAPI

from app.routers import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def leer_raiz():
    return {"mensaje": "¡Hola, mundo!"}