from abc import ABC, abstractmethod

class IStrategy(ABC):
    @abstractmethod
    def get_horario(self, user_id, cadastro_matricula, cadastro_cadeiras):
        pass

class ProfessorStrategy(IStrategy):
    def get_horario(self, user_id, cadastro_matricula, cadastro_cadeiras):
        cadeiras = cadastro_cadeiras.get_cadeiras_by_professor(user_id)
        return cadeiras

class AlunoStrategy(IStrategy):
    def get_horario(self, user_id, cadastro_matricula, cadastro_cadeiras):
        matricula = cadastro_matricula.get_current_by_aluno(user_id)
        return matricula.cadeiras
        