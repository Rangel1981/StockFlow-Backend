from fastapi import FastAPI
from database import criar_db_e_tabelas
from routes import product_routes, setor_routes # Importa suas rotas novas
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    criar_db_e_tabelas()
    yield

app = FastAPI(title="StockFlow - API", lifespan=lifespan)

app.include_router(setor_routes.router)

app.include_router(product_routes.router)

@app.get("/")
def home():
    return {"mensagem": "StockFlow online!", "Estrutura": "Modularizada!"} 