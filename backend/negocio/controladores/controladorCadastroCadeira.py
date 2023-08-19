from utils import SingletonMetaclass
from negocio.cadastros.cadastroCadeira import CadastroCadeira


class ControladorCadastroCadeira(metaclass=SingletonMetaclass):
    def __init__(self, cadastro_cadeira: CadastroCadeira) -> None:
        self.cadastro_cadeira = cadastro_cadeira

    def cadastrar_cadeira(self, data):
        nova_cadeira = self.cadastro_cadeira.cadastrar_cadeira(data)
        if nova_cadeira:
            return nova_cadeira
        else:
            return False

    def editar_cadeira(self, data):
        nova_cadeira = self.cadastro_cadeira.editar_cadeira(data)
        return nova_cadeira

    def deletar_cadeira(self, data):
        deleted = self.cadastro_cadeira.deletar_cadeira(data)
        return deleted
