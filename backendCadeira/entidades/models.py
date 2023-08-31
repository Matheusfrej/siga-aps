from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date, JSON
from datetime import date

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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
    ementa = Column(String, default='')

    prerequisitos = relationship('Cadeira', secondary=cadeira_prerequisito_association,
                                 primaryjoin='Cadeira.id==cadeira_prerequisito.c.cadeira_id',
                                 secondaryjoin='Cadeira.id==cadeira_prerequisito.c.prerequisito_id',
                                 backref='prerequisito_de')
    corequisitos = relationship('Cadeira', secondary=cadeira_corequisito_association,
                                primaryjoin='Cadeira.id==cadeira_corequisito.c.cadeira_id',
                                secondaryjoin='Cadeira.id==cadeira_corequisito.c.corequisito_id',
                                backref='corequisito_de')
    equivalencias = relationship('Cadeira', secondary=cadeira_equivalencia_association,
                                 primaryjoin='Cadeira.id==cadeira_equivalencia.c.cadeira_id',
                                 secondaryjoin='Cadeira.id==cadeira_equivalencia.c.equivalencia_id',
                                 backref='equivalencia_de')

    ofertas_cadeiras = relationship('OfertaCadeira', back_populates='cadeira')

    def __init__(
            self,
            nome: str,
            ementa: str = '',
            prerequisitos: list[int] = [],
            corequisitos: list[int] = [],
            equivalencias: list[int] = []):
        self.nome = nome
        self.ementa = ementa
        self.prerequisitos = prerequisitos
        self.corequisitos = corequisitos
        self.equivalencias = equivalencias


class OfertaCadeira(Base):
    __tablename__ = 'oferta_cadeira'

    id = Column(Integer, primary_key=True)

    horario = Column(JSON)
    plano_ensino = Column(String, default='')
    
    centro_universitario = Column(String)

    professor_id = Column(Integer)

    cadeira_id = Column(Integer, ForeignKey('cadeira.id'))
    cadeira = relationship('Cadeira', back_populates='ofertas_cadeiras')

    periodo = Column(String)

    def __init__(
            self,
            cadeira: int,
            horario: str,
            centro_universitario: str,
            professor_id: int,
            periodo: str,
            plano_ensino: str = ''):
        self.cadeira_id = cadeira
        self.horario = horario
        self.plano_ensino = plano_ensino
        self.centro_universitario = centro_universitario
        self.professor_id = professor_id
        self.periodo = periodo
