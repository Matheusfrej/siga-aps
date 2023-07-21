class Horario:
    def __init__(self, cadeiras):
        dicio = {
            'seg': dict(),
            'ter': dict(),
            'qua': dict(),
            'qui': dict(),
            'sex': dict(),
            'sab': dict(),
            'dom': dict()
        }

        for c in cadeiras:
            for k, v in c.horario.items():
                for h in v:
                    dicio[k][h] = c.nome

        self.data = dicio
