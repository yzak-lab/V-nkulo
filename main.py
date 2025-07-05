from fastapi import FastAPI
from routers import auth

app = FastAPI(
    title="Vínkulo API",
    description="Una API de autenticación simple utilizando FastAPI",
    version="0.1.0"
)

# Incluir routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/", tags=["root"])
def root():
    return {"mensaje": "Hola desde Vínkulo 🩵"}
