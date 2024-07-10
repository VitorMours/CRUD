from flask import current_app
from typing import Optional
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Criando banco de dados e migrações
db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):

    __tablename__ = 'User'

    id: Mapped[int] = db.Column(Integer, primary_key=True)
    name: Mapped[str] = db.Column(String(30))
    email: Mapped[str] = db.Column(String(100))
    password: Mapped[str] = db.Column(String(30))


    def __repr__(self) -> str:
        return f""


class Character(db.Model):
    __tablename__ = "Character"

    # First Page
    # Header of first Page
    id: Mapped[int] = db.Column(Integer, primary_key=True) 
    nome: Mapped[str] = db.Column(String(50))
    classe: Mapped[str] = db.Column(String(30)) 
    nivel: Mapped[int] = db.Column(Integer)
    antecedente: Mapped[str] = db.Column(String(30))

    # Verificar se deixo isso como chave estrangeira, ou não
      # nome_jogador: Mapped[int]

    raça: Mapped[str] = db.Column(String(20))
    alinhamento: Mapped[str] = db.Column(String(13))
    xp: Mapped[int] = db.Column(Integer)


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




class Table(db.Model):

    __tablename__ = 'Table'

    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(String(30))


    def __repr__(self) -> str:
        return f""





models_classes = [Table, User, Character]
