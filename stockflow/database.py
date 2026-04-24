import os
from sqlmodel import create_engine, SQLModel, Session

# O Docker passa esse endereço pra gente automaticamente
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def criar_db_e_tabelas():
    # Cria as tabelas baseadas nos modelos que importamos no main.py
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session