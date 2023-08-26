from entidades import Horario

class ControladorVisualizarHorario:
    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def get_horario(self, user_id):
        ofertas_cadeiras, cadeiras_dict = self.strategy.get_horario(user_id)
        return Horario(ofertas_cadeiras, cadeiras_dict)
