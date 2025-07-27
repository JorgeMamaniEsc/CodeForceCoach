from fastapi import FastAPI
from app.routers import users  # Importa el router de usuarios

app = FastAPI()

app.include_router(users.router)  # Añade el router de usuarios

@app.get("/")
async def root():
    return {"message": "¡CodeForceCoach funcionando!"}
