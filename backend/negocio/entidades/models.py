from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
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
    senha = Column(String)

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
            ano_entrada: str,
            senha: str) -> None:
        self.email = email
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.ano_entrada = ano_entrada
        self.senha = senha

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
    matriculas = relationship("Matricula", back_populates="aluno")

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
    cadeiras = relationship("Cadeira", back_populates="professor")

    def __init__(self, siape: str, formacao: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.siape = siape
        self.formacao = formacao


cadeira_prerequisito_association = Table(
    'cadeira_prerequisito',
    Base.metadata,
    Column('cadeira_id', Integer, ForeignKey('cadeira.id')),
    Column('prerequisito_id', Integer, ForeignKey('cadeira.id'))
)

cadeira_corequisito_association = Table(
    'cadeira_corequisito',
    Base.metadata,
    Column('cadeira_id', Integer, ForeignKey('cadeira.id')),
    Column('corequisito_id', Integer, ForeignKey('cadeira.id'))
)

cadeira_equivalencia_association = Table(
    'cadeira_equivalencia',
    Base.metadata,
    Column('cadeira_id', Integer, ForeignKey('cadeira.id')),
    Column('equivalencia_id', Integer, ForeignKey('cadeira.id'))
)


class Cadeira(Base):
    __tablename__ = 'cadeira'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    horario = Column(String)
    plano_ensino = Column(String, default='')
    centro_universitario = Column(String)

    prerequisitos = relationship("Cadeira", secondary=cadeira_prerequisito_association,
                                 primaryjoin="Cadeira.id==cadeira_prerequisito.c.cadeira_id",
                                 secondaryjoin="Cadeira.id==cadeira_prerequisito.c.prerequisito_id",
                                 backref="prerequisito_de")
    corequisitos = relationship("Cadeira", secondary=cadeira_corequisito_association,
                                primaryjoin="Cadeira.id==cadeira_corequisito.c.cadeira_id",
                                secondaryjoin="Cadeira.id==cadeira_corequisito.c.corequisito_id",
                                backref="corequisito_de")
    equivalencias = relationship("Cadeira", secondary=cadeira_equivalencia_association,
                                 primaryjoin="Cadeira.id==cadeira_equivalencia.c.cadeira_id",
                                 secondaryjoin="Cadeira.id==cadeira_equivalencia.c.equivalencia_id",
                                 backref="equivalencia_de")

    professor_id = Column(Integer, ForeignKey('conta_professor.id'))
    professor = relationship("ContaProfessor", back_populates="cadeiras")

    def __init__(
            self,
            nome: str,
            horario: str,
            centro_universitario: str,
            professor: int,
            plano_ensino: str = '',
            prerequisitos: list[int] = [],
            corequisitos: list[int] = [],
            equivalencias: list[int] = []):
        self.nome = nome
        self.horario = horario
        self.prerequisitos = prerequisitos
        self.corequisitos = corequisitos
        self.equivalencias = equivalencias
        self.plano_ensino = plano_ensino
        self.centro_universitario = centro_universitario
        self.professor_id = professor



matricula_cadeira_association = Table(
    'matricula_cadeira_association',
    Base.metadata,
    Column('matricula_id', Integer, ForeignKey('matricula.id')),
    Column('cadeira_id', Integer, ForeignKey('cadeira.id'))
)


class Matricula(Base):
    __tablename__ = 'matricula'

    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('conta_aluno.id'))
    periodo = Column(String)

    aluno = relationship("ContaAluno")
    cadeiras = relationship("Cadeira", secondary=matricula_cadeira_association)

    def __init__(
            self,
            aluno: int,
            cadeiras: list[int],
            periodo: str):
        self.aluno_id = aluno
        self.cadeiras = cadeiras
        self.periodo = periodo
