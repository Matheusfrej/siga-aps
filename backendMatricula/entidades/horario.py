class Horario:
    def __init__(self, ofertas_cadeiras_dicio):
        dicio = {
            'seg': dict(),
            'ter': dict(),
            'qua': dict(),
            'qui': dict(),
            'sex': dict(),
            'sab': dict(),
            'dom': dict()
        }

        for c in ofertas_cadeiras_dicio:
            for k, v in c.get('horario').items():
                for h in v:
                    dicio[k][h] = c.get('cadeira').get('nome')

        self.ofertas_cadeiras = ofertas_cadeiras_dicio
        self.data = dicio
