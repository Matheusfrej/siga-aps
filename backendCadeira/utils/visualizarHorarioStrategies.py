from abc import ABC, abstractmethod

class IStrategy(ABC):
    def __init__(self, cadastro) -> None:
        self.cadastro = cadastro

    @abstractmethod
    def get_horario(self, user_id):
        pass

class ProfessorStrategy(IStrategy):
    def __init__(self, cadastro_oferta_cadeiras, cadastro_cadeiras) -> None:
        self.cadastro_oferta_cadeiras = cadastro_oferta_cadeiras
        self.cadastro_cadeiras = cadastro_cadeiras

    def get_horario(self, user_id):
        ofertas_cadeiras = self.cadastro_oferta_cadeiras.get_ofertas_cadeiras_by_professor(user_id)
        cadeiras = self.cadastro_cadeiras.read_id_in_list([oferta.cadeira_id for oferta in ofertas_cadeiras])
        return ofertas_cadeiras, cadeiras