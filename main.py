from fastapi import FastAPI
from routers import auth

app = FastAPI()

app.include_router(auth.router)
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
  return {"message": "Hola desde Vínkulo"}
