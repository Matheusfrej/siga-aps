from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entidades import Base
from .repositorioContaSQLAlchemy import RepositorioContaSQLAlchemy
from .repositorioCadeiraSQLAlchemy import RepositorioCadeiraSQLAlchemy
from .repositorioMatriculaSQLAlchemy import RepositorioMatriculaSQLAlchemy


class SQLAlchemyRepositorioFactory:
    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///sigab.db")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def criar_repositorio_conta(self):
        return RepositorioContaSQLAlchemy(Session=self.Session)

    def criar_repositorio_cadeira(self):
        return RepositorioCadeiraSQLAlchemy(Session=self.Session)


    def criar_repositorio_matricula(self):
        return RepositorioMatriculaSQLAlchemy(Session=self.Session)
