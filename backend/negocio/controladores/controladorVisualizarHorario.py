from entidades import Horario

class ControladorVisualizarHorario:
    def __init__(self, cadastro_cadeira, cadastro_matricula, strategy) -> None:
        self.cadastro_cadeira = cadastro_cadeira
        self.cadastro_matricula = cadastro_matricula
        self.strategy = strategy()

    def get_horario(self, user_id):
        cadeiras = self.strategy.get_horario(user_id, self.cadastro_matricula, self.cadastro_cadeira)
        return Horario(cadeiras)

