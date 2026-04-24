from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from sqlmodel import Session
from database import criar_db_e_tabelas, get_session # Direto do arquivo database
from models.product_model import Produto

@asynccontextmanager
async def lifespan(app: FastAPI):
    criar_db_e_tabelas()
    yield

app = FastAPI(title="StockFlow - API", lifespan=lifespan)

@app.get("/")
def home():
    return {"Mensagem": "StockFlow Online!", "Status": "🚀"}

@app.post("/produtos/", response_model=Produto)
def criar_produto(produto: Produto, session: Session = Depends(get_session)):
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto