from dados import RepositorioCadeiraSQLAlchemy
from dados.iRepositorioCadeira import IRepositorioCadeira

class CadastroCadeira:
    def __init__(self):
        self.repositorio_cadeira: IRepositorioCadeira = RepositorioCadeiraSQLAlchemy()

    def cadastrar_cadeira(self, data):
        cadeira = self.repositorio_cadeira.create(data)
        return cadeira

    def editar_cadeira(self, data):
        cadeira = self.repositorio_cadeira.update(data)
        return cadeira
    
    def deletar_cadeira(self, data):
        cadeira = self.repositorio_cadeira.delete(data)
        return cadeira

    def get_cadeira_by_professor(self, professor_id):
        cadeiras = self.repositorio_cadeira.get_by_professor(professor_id)
        return cadeiras