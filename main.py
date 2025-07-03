from fastapi import FastAPI
from routers import Auth

app = FastAPI()
app.include_router(Auth.enrutador)
@app.get("/")
def root():
  return {"mensaje": "Hola desde Vínkulo 🩵"}
