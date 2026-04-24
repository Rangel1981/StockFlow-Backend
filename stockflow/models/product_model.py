from sqlmodel import SQLModel, Field
from typing import Optional


class Produto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: Optional[str] = None
    preco_custo: float  
    preco_venda: float
    quantidade: int