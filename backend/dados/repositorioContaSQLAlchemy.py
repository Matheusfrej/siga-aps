from .iRepositorioConta import IRepositorioConta
from entidades import ContaBase, ContaAluno, ContaProfessor
from sqlalchemy.orm import joinedload

class RepositorioContaSQLAlchemy(IRepositorioConta):
    def __init__(self, Session):
        self.Session = Session

    def create(self, data):
        with self.Session() as session:
            nova_conta = ContaBase(**data)
            session.add(nova_conta)
            session.commit()
            return nova_conta

    def create_aluno(self, data):
        with self.Session() as session:
            nova_conta = ContaAluno(**data)
            session.add(nova_conta)
            session.commit()
            return nova_conta

    def create_professor(self, data):
        with self.Session() as session:
            nova_conta = ContaProfessor(**data)
            session.add(nova_conta)
            session.commit()
            return nova_conta

    def read(self, id):
        with self.Session() as session:
            return session.query(ContaBase).filter_by(id=id).first()

    def update(self, id, data):
        with self.Session() as session:
            conta = session.query(ContaBase).filter_by(id=id).first()
            if conta:
                # print(conta)
                # for key, value in data.items():
                #     setattr(conta, key, value)
                # session.commit()
                pass
            else:
                #TODO lembrar de levantar um erro caso a conta não exista
                pass

    def delete(self, id):
        with self.Session() as session:
            conta = session.query(ContaBase).filter_by(id=id).first()
            if conta:
                session.delete(conta)
                session.commit()
                return True
            else:
                # TODO fazer um raise
                return False

    def get_by_email(self, email):
        with self.Session() as session:
            return session.query(ContaBase).filter_by(email=email).options(joinedload('*')).first()
