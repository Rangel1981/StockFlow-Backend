from sqlmodel import SQLModel, Field, Relationship # Garanta que Relationship esteja aqui
from typing import Optional

class Produto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    preco_custo: float
    preco_venda: float
    quantidade: int

    # 1. A CHAVE ESTRANGEIRA (O "link" no banco de dados)
    setor_id: Optional[int] = Field(default=None, foreign_key="setor.id")

    # 2. O RELACIONAMENTO (O "atalho" para o Python)
    setor: Optional["Setor"] = Relationship(back_populates="produtos")