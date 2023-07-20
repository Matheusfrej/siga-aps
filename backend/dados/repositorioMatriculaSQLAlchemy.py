from dados.iRepositorioConta import IRepositorioMatricula
from negocio.entidades import ContaAluno, Matricula

from datetime import date

class RepositorioMatriculaLocal(IRepositorioMatricula):
    def __init__(self):
        pass

    def get_by_id(self, id: int):
        pass
    
    def get_by_aluno(self, id_aluno: int):
        pass

    def fazer_matricula(self, aluno: int, cadeiras: list, periodo: str):
        pass

    def validar_matricula(self, matricula: Matricula):
        pass