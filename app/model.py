from typing import Optional
from flask import Flask 
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = 'User'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    email: Mapped[str] = mapped_column(String(100))

    def __repr__(self) -> str:
        return f""


class Character(Base):
    __tablename__ = "Character"

    # First Page
    # Header of first Page
    id: Mapped[int] = mapped_column(primary_key=True) 
    nome: Mapped[str] = mapped_column(String(50))
    classe: Mapped[str] = mapped_column(String(30)) 
    nivel: Mapped[int] = mapped_column()
    antecedente: Mapped[str] = mapped_column(String(30))
    
    # Verificar se deixo isso como chave estrangeira, ou não
      # nome_jogador: Mapped[int]
    
    raça: Mapped[str] = mapped_column(String(20))
    alinhamento: Mapped[str] = mapped_column(String(13))
    xp: Mapped[int] = mapped_column()
    

    # Attributes
    forca: Mapped[int] = mapped_column()
    destreza: Mapped[int] = mapped_column() 
    constituicao: Mapped[int] = mapped_column()
    inteligencia: Mapped[int] = mapped_column()
    sabedoria: Mapped[int] = mapped_column()
    carisma: Mapped[int] = mapped_column()


    #Second Page


    # Character attributes
    inspiracao: Mapped[int] = mapped_column()
    bonus_proeficiencia: Mapped[int] = mapped_column()
    classe_armadura: Mapped[int] = mapped_column()
    iniciativa: Mapped[int] = mapped_column()
    deslocamento: Mapped[int] = mapped_column()
    pontos_vida_atual: Mapped[int] = mapped_column()
    pontos_vida_temporario: Mapped[int] = mapped_column()
    dados_de_vida: Mapped[int] = mapped_column()
    salva_guarda: Mapped[int] = mapped_column()




class Table(Base):
    
    __tablename__ = 'Table'

    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(String(30))


    def __repr__(self) -> str:
        return f""
    





