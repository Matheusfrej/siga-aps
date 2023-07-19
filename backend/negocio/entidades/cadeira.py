class Cadeira:
    def __init__(
            self,
            id: int,
            nome: str,
            horario: str,
            centro_universitario: str,
            professor: int,
            plano_ensino: str='',
            prerequisitos: list[int]=[],
            corequisitos: list[int]=[],
            equivalencias: list[int]=[]):
        self.id = id
        self.nome = nome
        self.horario = horario
        self.prerequisitos = prerequisitos
        self.corequisitos = corequisitos
        self.equivalencias = equivalencias
        self.plano_ensino = plano_ensino
        self.centro_universitario = centro_universitario
        self.professor = professor