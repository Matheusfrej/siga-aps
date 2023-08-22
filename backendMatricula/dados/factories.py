from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entidades import Base
from .repositorioMatriculaLocal import RepositorioMatriculaLocal
from .repositorioMatriculaSQLAlchemy import RepositorioMatriculaSQLAlchemy

from abc import ABC, abstractmethod

class AbstractRepositorioFactory(ABC):
    @abstractmethod
    def criar_repositorio_matricula(self):
        pass

class SQLAlchemyRepositorioFactory(AbstractRepositorioFactory):
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///sigab.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def criar_repositorio_matricula(self):
        return RepositorioMatriculaSQLAlchemy(Session=self.Session)

class ListRepositorioFactory:

    def criar_repositorio_matricula(self):
        return RepositorioMatriculaLocal()
