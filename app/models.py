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
    forca: Mapped[int] = db.Column()
    destreza: Mapped[int] = db.Column() 
    constituicao: Mapped[int] = db.Column()
    inteligencia: Mapped[int] = db.Column()
    sabedoria: Mapped[int] = db.Column()
    carisma: Mapped[int] = db.Column()


    #Second Page


    # Character attributes
    inspiracao: Mapped[int] = db.Column()
    bonus_proeficiencia: Mapped[int] = db.Column()
    classe_armadura: Mapped[int] = db.Column()
    iniciativa: Mapped[int] = db.Column()
    deslocamento: Mapped[int] = db.Column()
    pontos_vida_atual: Mapped[int] = db.Column()
    pontos_vida_temporario: Mapped[int] = db.Column()
    dados_de_vida: Mapped[int] = db.Column()
    salva_guarda: Mapped[int] = db.Column()




class Table(db.Model):

    __tablename__ = 'Table'

    id: Mapped[int] = db.Column(Integer, primary_key=True)
    owner: Mapped[str] = db.Column(String(30))
    publicity: Mapped[bool] = db.Column()

    def __repr__(self) -> str:
        return f""





