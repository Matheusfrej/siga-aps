from dados.iRepositorioConta import IRepositorioMatricula
from entidades import ContaAluno, Matricula

from datetime import date

class RepositorioMatriculaLocal(IRepositorioMatricula):
    def __init__(self):
        self._matriculas = [Matricula(id=1, aluno=1, cadeiras=[1], periodo="2023.1")]
        self._count = len(self._matriculas)

    def get_by_id(self, id: int):
        return list(filter(lambda x: x.id == id, self._matriculas))[0]
    
    def get_by_aluno(self, id_aluno: int):
        return list(filter(lambda x: x.aluno.id == id_aluno, self._matriculas))
    
    def fazer_matricula(self, aluno: int, cadeiras: list, periodo: str):
        nova_matricula = Matricula(id=2,aluno=aluno,cadeiras=cadeiras,periodo=periodo)
        validar = self.validar_matricula(nova_matricula)
        if validar:
            self._matriculas.append(nova_matricula)
            self._count += 1
            return nova_matricula
        else:
            pass

    def validar_matricula(self, matricula: Matricula):
        return True