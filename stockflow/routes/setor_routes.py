from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from database import get_session
from models.setor_model import Setor

router = APIRouter(prefix="/setores", tags=["setores"])

#criar rota para os setores
@router.post("/", response_model=Setor)
def criar_setor(setor: Setor, session: Session = Depends(get_session)):
    session.add(setor)
    session.commit()
    session.refresh(setor)
    return setor

# ROTA PARA LISTAR SETORES

@router.get("/", response_model=List[Setor])
def listar_setores(session: Session = Depends(get_session)):
    return session.exec(select(Setor)).all()


@router.delete("/{setor_id}")
def deletar_setor(setor_id: int, session: Session = Depends(get_session)):
    #procurando o setor pelo id
    db_setor = session.get(Setor, setor_id)

    # E SE o setor não existir 
    if not db_setor:
        raise HTTPException(status_code=404, detail="Nenhum setor foi localizado com esse id")
    
    #caso encontre o setor
    session.delete(db_setor)

    #salvar a alteração no banco de dados
    session.commit()
    return {"mensagem": f"O Setor '{db_setor}' removido com sucesso"}