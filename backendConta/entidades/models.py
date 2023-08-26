from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date, JSON
from datetime import date

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ContaBase(Base):
    __tablename__ = 'conta_base'
    
    id = Column(Integer, primary_key=True)
    email = Column(String)
    cpf = Column(String)
    nome = Column(String)
    data_nascimento = Column(Date)
    ano_entrada = Column(String)

    discriminator = Column(String)  # Discriminator column for identifying user types
    __mapper_args__ = {
        'polymorphic_identity': 'conta_base',
        'polymorphic_on': discriminator
    }

    def __init__(
            self,
            email: str,
            cpf: str,
            nome: str,
            data_nascimento: date,
            ano_entrada: str) -> None:
        self.email = email
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.ano_entrada = ano_entrada

    def __repr__(self) -> str:
        return f'<User {self.id}: {self.email}>'


class ContaAluno(ContaBase):
    __tablename__ = 'conta_aluno'
    
    id = Column(Integer, ForeignKey('conta_base.id'), primary_key=True)
    curso = Column(String)

    discriminator = Column(String, default='conta_aluno')
    __mapper_args__ = {
        'polymorphic_identity': 'conta_aluno',
    }

    def __init__(self, curso: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.curso = curso


class ContaProfessor(ContaBase):
    __tablename__ = 'conta_professor'

    id = Column(Integer, ForeignKey('conta_base.id'), primary_key=True)
    siape = Column(String)
    formacao = Column(String)
    discriminator = Column(String, default='conta_professor')
    __mapper_args__ = {
        'polymorphic_identity': 'conta_professor',
    }

    def __init__(self, siape: str, formacao: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.siape = siape
        self.formacao = formacao
