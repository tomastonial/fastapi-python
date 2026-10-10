from fastapi import FastAPI
import os
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/", response_class=HTMLResponse)
def inicio():
    return """
    <h1>Bem-vindo à API!</h1>
    <a href="/docs">Documentação da API</a><br>
    <a href="/health">Health</a><br>
    <a href="/config/envs">Variáveis de ambiente</a>
    """

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/config/envs")
def get_envs():
    return{
        "ambiente": os.getenv("AMBIENTE"),
        "versao": os.getenv("VERSION")
    }

@app.post("/items/")
def create_item(items: list[Item]):
    return {"items": items}