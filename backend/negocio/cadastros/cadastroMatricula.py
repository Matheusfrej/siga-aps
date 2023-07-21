from dados import RepositorioMatriculaSQLAlchemy
from dados import IRepositorioMatricula

class CadastroMatricula:
    def __init__(self):
        self.repositorio_matricula: IRepositorioMatricula = RepositorioMatriculaSQLAlchemy()

    def get_current_by_aluno(self, aluno_id):
        print(aluno_id)
        matricula = self.repositorio_matricula.get_current_by_aluno(aluno_id)
        return matricula
