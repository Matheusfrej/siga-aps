from .iRepositorioMatricula import IRepositorioMatricula
from sqlalchemy.orm import joinedload
from entidades import Matricula

from datetime import datetime


class RepositorioMatriculaSQLAlchemy(IRepositorioMatricula):
    def __init__(self, Session):
        self.Session = Session

    def create(self, data):
        with self.Session() as session:
            nova_matricula = Matricula(**data)
            session.add(nova_matricula)
            session.commit()
            nova_matricula = session.query(Matricula).filter_by(
                id=nova_matricula.id).first()
            return nova_matricula
    
    def get_by_id(self, id):
        with self.Session() as session:
            return session.query(Matricula).filter_by(id=id).first()
    
    def update(self, id, data):
        with self.Session() as session:
            matricula = session.query(Matricula).filter_by(id=id).first()
            if matricula:
                # print(matricula)
                # for key, value in data.items():
                #     setattr(matricula, key, value)
                # session.commit()
                pass
            else:
                #TODO lembrar de levantar um erro caso a matricula não exista
                pass
    
    def delete(self, id):
        with self.Session() as session:
            matricula = session.query(Matricula).filter_by(id=id).first()
            if matricula:
                session.delete(matricula)
                session.commit()
            else:
                #TODO lembrar de levantar um erro caso a matricula não exista
                pass

    def get_by_aluno(self, id_aluno):
        with self.Session() as session:
            matriculas = session.query(Matricula).filter_by(aluno_id=id_aluno)
            return list(matriculas)

    def get_current_by_aluno(self, id_aluno):
        with self.Session() as session:
            matriculas = session.query(
                Matricula).filter_by(aluno_id=id_aluno)
            curr_date = datetime.now()
            year = curr_date.year
            month = curr_date.month
            periodo = f'{year}.{1 if month <= 6 else 2}'
            matricula = matriculas.filter_by(periodo=periodo).first()
            return matricula
