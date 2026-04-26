from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from database import get_session
from models.product_model import Produto

router = APIRouter(prefix="/produtos", tags=["Produto"])


@router.post("/", response_model=Produto)
def criar_produto(produto: Produto, session: Session = Depends(get_session)):
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto

@router.get("/", response_model=List[Produto])
def listar_produtos(session: Session = Depends(get_session)):
    # O select busca todos os registros da tabela Produto no banco
    produtos = session.exec(select(Produto)).all()
    return produtos

@router.get("/{produtos_id}", response_model=Produto)
def buscar_pelo_id(produto_id: int, session: Session = Depends(get_session)):
    produto = session.get(Produto, produto_id)

    # E SE não existir o id
    if not produto:
        raise HTTPException(status_code=404, detail= "Nenhum produto foi encontrado com esse id")
    
    return produto

@router.delete("/{produto_id}")
def deletar_produto(produto_id: int, session: Session = Depends(get_session)):
    #procurando produto pelo id
    db_produto = session.get(Produto, produto_id)

    #E SE o produto não existir
    if not db_produto:
        raise HTTPException(status_code=404, detail="Nenhum produto foi encontrado com esse id")

    # caso encontre, manda deletar
    session.delete(db_produto)

    #Salvar a alteração no banco de dados
    session.commit()
    return {"mensagem": f"Produto '{db_produto.nome}' removido com sucesso!"}

@router.patch("/{produto_id}", response_model=Produto)
def atualizar_produto(produto_id: int,
                      produto_recebido: Produto,
                      session: Session = Depends(get_session)):
    
    produto_banco = session.get(Produto, produto_id)

    #E se o produto não existir
    if not produto_banco:
        raise HTTPException(status_code=404, detail="Nenhum produto foi encontrado com esse id")
    
    # Transforma o que veio do Swagger em um dicionário (ignorando o que não foi preenchido)
    dados_novos = produto_recebido.model_dump(exclude_unset=True)

    #loop para atualizar cada campo automaticamente
    for chave, valor in dados_novos.items():
        setattr(produto_banco, chave, valor)

    #salvar e atualizar o objeto
    session.add(produto_banco)
    session.commit()
    session.refresh(produto_banco)
       
    return produto_banco #retorna o produto já atualizado