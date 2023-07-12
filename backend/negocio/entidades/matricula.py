from .conta import ContaAluno

class Matricula:
    def __init__(
            self,
            id: int,
            aluno: int,
            cadeiras: list[int],
            periodo: str):
        id = id
        aluno = aluno
        cadeiras = cadeiras
        periodo = periodo