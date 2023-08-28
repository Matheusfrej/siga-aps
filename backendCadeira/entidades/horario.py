class Horario:
    def __init__(self, ofertas_cadeiras, dicio_cadeiras):
        dicio = {
            'seg': dict(),
            'ter': dict(),
            'qua': dict(),
            'qui': dict(),
            'sex': dict(),
            'sab': dict(),
            'dom': dict()
        }
        for c in ofertas_cadeiras:
            for k, v in c.horario.items():
                for h in v:
                    dicio[k][h] = dicio_cadeiras.get(c.cadeira_id).nome

        self.ofertas_cadeiras = ofertas_cadeiras
        self.data = dicio
