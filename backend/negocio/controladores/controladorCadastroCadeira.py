from utils.singleton import SingletonMetaclass
from negocio.cadastros.cadastroCadeira import CadastroCadeira
from negocio.cadastros.cadastroConta import CadastroConta


class ControladorCadastroCadeira(metaclass=SingletonMetaclass):
    def __init__(self, cadastro_cadeira: CadastroCadeira, cadastro_conta: CadastroConta) -> None:
        self.cadastro_cadeira = cadastro_cadeira
        self.cadastro_conta = cadastro_conta

    def cadastrar_cadeira(self, data):
        nova_cadeira = self.cadastro_cadeira.cadastrar_cadeira(data)
        return nova_cadeira