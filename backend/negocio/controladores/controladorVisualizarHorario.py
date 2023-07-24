from entidades import Horario

class ControladorVisualizarHorario:
    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def get_horario(self, user_id):
        cadeiras = self.strategy.get_horario(user_id)
        return Horario(cadeiras)
