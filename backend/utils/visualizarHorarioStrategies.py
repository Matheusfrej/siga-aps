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

class AlunoStrategy(IStrategy):
    def __init__(self, cadastro_matricula, cadastro_cadeiras, cadastro_oferta_cadeiras) -> None:
        self.cadastro_matricula = cadastro_matricula
        self.cadastro_cadeiras = cadastro_cadeiras
        self.cadastro_oferta_cadeiras = cadastro_oferta_cadeiras

    def get_horario(self, user_id):
        matricula = self.cadastro_matricula.get_current_by_aluno(user_id)
        oferta_cadeiras = self.cadastro_oferta_cadeiras.read_id_in_list([a.id for a in list(matricula.ofertas_cadeiras)])
        cadeiras = self.cadastro_cadeiras.read_id_in_list([oferta for oferta in oferta_cadeiras.keys()])
        return oferta_cadeiras.values(), cadeiras
        