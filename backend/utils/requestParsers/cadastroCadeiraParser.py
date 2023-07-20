from flask_restful import reqparse

class CadastroCadeiraRequestParser(reqparse.RequestParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_argument('nome', type=str, required=True)
        self.add_argument('horario', type=str, required=True)
        self.add_argument('prerequisitos', type=list)
        self.add_argument('corequisitos', type=list)
        self.add_argument('equivalencias', type=list)
        self.add_argument('plano_ensino', type=str)
        self.add_argument('centro_universitario', type=str, required=True)
        self.add_argument('professor', type=int, required=True)