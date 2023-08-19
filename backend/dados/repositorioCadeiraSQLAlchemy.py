from .iRepositorioCadeira import IRepositorioCadeira
from entidades import Cadeira
from sqlalchemy.orm import joinedload

class RepositorioCadeiraSQLAlchemy(IRepositorioCadeira):
    def __init__(self, Session):
        self.Session = Session

    def create(self, data):
        with self.Session() as session:
            nova_cadeira = Cadeira(**data)
            session.add(nova_cadeira)
            session.commit()
            nova_cadeira = session.query(Cadeira).filter_by(id=nova_cadeira.id).options(joinedload('*')).first()
            return nova_cadeira

    def read(self, id):
        with self.Session() as session:
            return session.query(Cadeira).filter_by(id=id).first()

    def update(self, id, data):
        with self.Session() as session:
            cadeira = session.query(Cadeira).filter_by(id=id).first()
            if cadeira:
                for key, value in data.items():
                    setattr(cadeira, key, value)
                session.commit()
            else:
                #TODO lembrar de levantar um erro caso a cadeira não exista
                pass

    def delete(self, id):
        with self.Session() as session:
            cadeira = session.query(Cadeira).filter_by(id=id).first()
            if cadeira:
                session.delete(cadeira)
                session.commit()
                return True
            else:
                # TODO fazer um raise
                return False
