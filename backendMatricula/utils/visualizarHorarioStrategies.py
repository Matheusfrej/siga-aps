from abc import ABC, abstractmethod
from comunicacao.CadeiraServiceApi import CadeiraServiceApi

class IStrategy(ABC):
    def __init__(self, cadastro) -> None:
        self.cadastro = cadastro

    @abstractmethod
    def get_horario(self, user_id):
        pass

class AlunoStrategy(IStrategy):
    def __init__(self, cadastro_matricula) -> None:
        self.cadastro_matricula = cadastro_matricula
        self.cadeira_service = CadeiraServiceApi()

    def get_horario(self, user_id):
        matricula = self.cadastro_matricula.get_current_by_aluno(user_id)
        cadeiras_entities = []
        for id in matricula.cadeiras:
            cadeira = self.cadeira_service.get_oferta_cadeira_by_id(id)
            cadeiras_entities.append(cadeira)
        return cadeiras_entities
        