from sqlalchemy import Column, Integer, String
from sqlalchemy import PickleType

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Matricula(Base):
    __tablename__ = 'matricula'

    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer)
    cadeiras = Column(PickleType) #o pickle type serializa e deserializa objetos python com pickle.dumps() to incoming objects, and pickle.loads() on the way out
    periodo = Column(String)

    def __init__(
            self,
            aluno: int,
            cadeiras: list[int],
            periodo: str):
        self.aluno_id = aluno
        self.cadeiras = cadeiras
        self.periodo = periodo
