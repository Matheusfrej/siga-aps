from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entidades import Base
from .repositorioContaLocal import RepositorioContaLocal
from .repositorioContaSQLAlchemy import RepositorioContaSQLAlchemy

from abc import ABC, abstractmethod

class AbstractRepositorioFactory(ABC):
    @abstractmethod
    def criar_repositorio_conta(self):
        pass

class SQLAlchemyRepositorioFactory(AbstractRepositorioFactory):
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///sigab.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def criar_repositorio_conta(self):
        return RepositorioContaSQLAlchemy(Session=self.Session)

class ListRepositorioFactory:
    def criar_repositorio_conta(self):
        return RepositorioContaLocal()
