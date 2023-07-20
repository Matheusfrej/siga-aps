from dados.iRepositorioConta import IRepositorioMatricula
from negocio.entidades import ContaAluno

from datetime import date

class RepositorioMatriculaLocal(IRepositorioMatricula):
    def __init__(self):
        self._matriculas = [ContaAluno(curso='Ciência da Computação', id=1, email='fgm3@cin.ufpe.br', cpf='09265297492', nome='Filipe Gomes de Melo', data_nascimento=date(2002, 2, 28), ano_entrada='2020.1', senha='senha123*')]
        self._count = len(self._matriculas)

    def get_by_id(self, id):
        return list(filter(lambda x: x.id == id, self._matriculas))[0]
    
    def get_by_aluno(self, id_aluno):
        return list(filter(lambda x: x.aluno.id == id_aluno, self._matriculas))[0]