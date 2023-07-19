from utils.singleton import SingletonMetaclass
from dados.iRepositorioCadeira import IRepositorioCadeira
from dados.iRepositorioConta import IRepositorioConta


class ControladorCadastroCadeira(metaclass=SingletonMetaclass):
    def __init__(self, cadastro_cadeira: IRepositorioCadeira, cadastro_conta: IRepositorioConta) -> None:
        self.cadastro_cadeira = cadastro_cadeira
        self.cadastro_conta = cadastro_conta

    def cadastrar_cadeira(self, *args, **kwargs):
        nova_cadeira = self.cadastro_cadeira.cadastrar_cadeira(*args, **kwargs)
        return nova_cadeira