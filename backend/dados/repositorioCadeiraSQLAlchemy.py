from dados.iRepositorioCadeira import IRepositorioCadeira
from entidades import Cadeira, Session


class RepositorioCadeiraSQLAlchemy(IRepositorioCadeira):
    def __init__(self):
        self.Session = Session

    def create(self, data):
        with self.Session() as session:
            nova_cadeira = Cadeira(**data)
            session.add(nova_cadeira)
            session.commit()
            return nova_cadeira

    def read(self, id):
        with self.Session() as session:
            return session.query(Cadeira).filter_by(id=id).first()

    def update(self, id, data):
        with self.Session() as session:
            cadeira = session.query(Cadeira).filter_by(id=id).first()
            if cadeira:
                # print(cadeira)
                # for key, value in data.items():
                #     setattr(cadeira, key, value)
                # session.commit()
                pass
            else:
                #TODO lembrar de levantar um erro caso a cadeira não exista
                pass

    def delete(self, id):
        with self.Session() as session:
            cadeira = session.query(Cadeira).filter_by(id=id).first()
            if cadeira:
                session.delete(cadeira)
                session.commit()
            else:
                pass

    def validar_cadeira(self, data):
        pass

    def get_by_professor(self, professor_id):
        with self.Session() as session:
            cadeiras = session.query(Cadeira).filter_by(professor_id=professor_id)
            print(cadeiras)
            return list(cadeiras)


