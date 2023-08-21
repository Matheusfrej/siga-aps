from abc import ABC, abstractmethod

class IStrategy(ABC):
    def __init__(self, cadastro) -> None:
        self.cadastro = cadastro

    @abstractmethod
    def get_horario(self, user_id):
        pass

class AlunoStrategy(IStrategy):
    def __init__(self, cadastro_matricula) -> None:
        self.cadastro_matricula = cadastro_matricula

    def get_horario(self, user_id):
        matricula = self.cadastro_matricula.get_current_by_aluno(user_id)
        return matricula.ofertas_cadeiras
        