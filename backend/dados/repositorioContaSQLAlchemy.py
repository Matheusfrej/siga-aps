from dados.iRepositorioConta import IRepositorioConta
from negocio.entidades import ContaBase, ContaAluno, ContaProfessor, Session

class RepositorioContaSQLAlchemy(IRepositorioConta):
    def __init__(self):
        self.Session = Session

    def create(self, data):
        with Session() as session:
            nova_conta = ContaBase(**data)
            session.add(nova_conta)
            session.commit()

    def create_aluno(self, data):
        with Session() as session:
            nova_conta = ContaAluno(**data)
            session.add(nova_conta)
            session.commit()

    def create_professor(self, data):
        with Session() as session:
            nova_conta = ContaProfessor(**data)
            session.add(nova_conta)
            session.commit()

    def read(self, id):
        with Session() as session:
            return session.query(ContaBase).filter_by(id=id).first()

    def update(self, id, data):
        with Session() as session:
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
        with Session() as session:
            conta = session.query(ContaBase).filter_by(id=id).first()
            if conta:
                session.delete(conta)
                session.commit()
            else:
                pass

    def get_by_email(self, email):
        with Session() as session:
            return session.query(ContaBase).filter_by(email=email).first()