from flask import current_app
from typing import Optional
from sqlalchemy import Integer, String, Boolean, ForeignKey
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
    email: Mapped[str] = db.Column(String(100), unique=True)
    password: Mapped[str] = db.Column(String(30))


    def __repr__(self) -> str:
        return f"<User {self.id} {self.name} {self.email} {self.password}>"


class Character(db.Model):
    __tablename__ = "Character"

    # First Page
    # Meta Information
    id: Mapped[int] = db.Column(Integer, primary_key=True) 
    owner: Mapped[str] = db.Column(ForeignKey(User.id))    
    # Header of first Page
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
    forca: Mapped[int] = db.Column(Integer)
    destreza: Mapped[int] = db.Column(Integer) 
    constituicao: Mapped[int] = db.Column(Integer)
    inteligencia: Mapped[int] = db.Column(Integer)
    sabedoria: Mapped[int] = db.Column(Integer)
    carisma: Mapped[int] = db.Column(Integer)


    #Second Page


    # Character attributes
    inspiracao: Mapped[int] = db.Column(Integer)
    bonus_proeficiencia: Mapped[int] = db.Column(Integer)
    classe_armadura: Mapped[int] = db.Column(Integer)
    iniciativa: Mapped[int] = db.Column(Integer)
    deslocamento: Mapped[int] = db.Column(Integer)
    pontos_vida_atual: Mapped[int] = db.Column(Integer)
    pontos_vida_temporario: Mapped[int] = db.Column(Integer)
    dados_de_vida: Mapped[int] = db.Column(Integer)
    salva_guarda: Mapped[int] = db.Column(Integer)




class Table(db.Model):

    __tablename__ = 'Table'

    id: Mapped[int] = db.Column(Integer, primary_key=True)
    owner: Mapped[str] = db.Column(String(30))
    publicity: Mapped[bool] = db.Column(Boolean)

    def __repr__(self) -> str:
        return f""

