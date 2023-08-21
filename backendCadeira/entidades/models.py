from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date, JSON
from datetime import date

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cadeira(Base):
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
    def __init__(
            self,
            cadeira: int,
            horario: str,
            centro_universitario: str,
            professor: int,
            periodo: str,
            plano_ensino: str = ''):
        self.cadeira_id = cadeira
        self.horario = horario
        self.plano_ensino = plano_ensino
        self.centro_universitario = centro_universitario
        self.professor_id = professor
        self.periodo = periodo
