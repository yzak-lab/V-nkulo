from fastapi import FastAPI
from routers import auth

app = FastAPI()
app.include_router(auth.enrutador)
@app.get("/")
def root():
  return {"mensaje": "Hola desde Vínkulo 🩵"}
