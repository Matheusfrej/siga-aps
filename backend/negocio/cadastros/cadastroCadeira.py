from dados import RepositorioCadeiraLocal
from dados.iRepositorioCadeira import IRepositorioCadeira

class CadastroCadeira:
    def __init__(self):
        self.repositorio_cadeira: IRepositorioCadeira = RepositorioCadeiraLocal()

    def cadastrar_cadeira(self, *args, **kwargs):
        cadeira = self.repositorio_cadeira.cadastrar_cadeira(*args, **kwargs)
        return cadeira