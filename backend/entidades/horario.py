class Horario:
    def __init__(self, cadeiras):
        print(cadeiras)
        dicio = {
            'seg': [],
            'ter': [],
            'qua': [],
            'qui': [],
            'sex': [],
            'sab': [],
            'dom': []
        }

        for c in cadeiras:
            for k, v in c.horario.items():
                dicio[k] += v
        
        for k, v in dicio.items():
            v.sort()

        self.data = dicio
        print(self.data)
