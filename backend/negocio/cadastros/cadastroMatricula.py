from dados import IRepositorioMatricula
from utils import SingletonMetaclass


class CadastroMatricula(metaclass=SingletonMetaclass):
    def __init__(self, repositorio_matricula):
        self.repositorio_matricula: IRepositorioMatricula = repositorio_matricula

    def get_current_by_aluno(self, aluno_id):
        matricula = self.repositorio_matricula.get_current_by_aluno(aluno_id)
        return matricula
