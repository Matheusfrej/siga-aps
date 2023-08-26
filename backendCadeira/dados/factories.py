from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entidades import Base
from .repositorioCadeiraSQLAlchemy import RepositorioCadeiraSQLAlchemy
from .repositorioOfertaCadeiraSQLAlchemy import RepositorioOfertaCadeiraSQLAlchemy
from .repositorioCadeiraLocal import RepositorioCadeiraLocal
from .repositorioOfertaCadeiraLocal import RepositorioOfertaCadeiraLocal

from abc import ABC, abstractmethod

class AbstractRepositorioFactory(ABC):
    @abstractmethod
    def criar_repositorio_cadeira(self):
        pass

    @abstractmethod
    def criar_repositorio_oferta_cadeira(self):
        pass

class SQLAlchemyRepositorioFactory(AbstractRepositorioFactory):
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///sigab.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def criar_repositorio_cadeira(self):
        return RepositorioCadeiraSQLAlchemy(Session=self.Session)

    def criar_repositorio_oferta_cadeira(self):
        return RepositorioOfertaCadeiraSQLAlchemy(Session=self.Session)

class ListRepositorioFactory:
    def criar_repositorio_cadeira(self):
        return RepositorioCadeiraLocal()

    def criar_repositorio_oferta_cadeira(self):
        return RepositorioOfertaCadeiraLocal()
