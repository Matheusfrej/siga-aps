from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entidades import Base
from .repositorioContaSQLAlchemy import RepositorioContaSQLAlchemy
from .repositorioCadeiraSQLAlchemy import RepositorioCadeiraSQLAlchemy
from .repositorioMatriculaSQLAlchemy import RepositorioMatriculaSQLAlchemy
from .repositorioOfertaCadeiraSQLAlchemy import RepositorioOfertaCadeiraSQLAlchemy
from .repositorioContaLocal import RepositorioContaLocal
from .repositorioCadeiraLocal import RepositorioCadeiraLocal
from .repositorioMatriculaLocal import RepositorioMatriculaLocal
from .repositorioOfertaCadeiraLocal import RepositorioOfertaCadeiraLocal

from abc import ABC, abstractmethod

class AbstractRepositorioFactory(ABC):
    @abstractmethod
    def criar_repositorio_conta(self):
        pass

    @abstractmethod
    def criar_repositorio_cadeira(self):
        pass

    @abstractmethod
    def criar_repositorio_matricula(self):
        pass

    @abstractmethod
    def criar_repositorio_oferta_cadeira(self):
        pass

class SQLAlchemyRepositorioFactory(AbstractRepositorioFactory):
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///sigab.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def criar_repositorio_conta(self):
        return RepositorioContaSQLAlchemy(Session=self.Session)

    def criar_repositorio_cadeira(self):
        return RepositorioCadeiraSQLAlchemy(Session=self.Session)

    def criar_repositorio_matricula(self):
        return RepositorioMatriculaSQLAlchemy(Session=self.Session)

    def criar_repositorio_oferta_cadeira(self):
        return RepositorioOfertaCadeiraSQLAlchemy(Session=self.Session)

class ListRepositorioFactory:
    def criar_repositorio_conta(self):
        return RepositorioContaLocal()

    def criar_repositorio_cadeira(self):
        return RepositorioCadeiraLocal()

    def criar_repositorio_matricula(self):
        return RepositorioMatriculaLocal()

    def criar_repositorio_oferta_cadeira(self):
        return RepositorioOfertaCadeiraLocal()
