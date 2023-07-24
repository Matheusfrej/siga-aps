from utils import SingletonMetaclass
from negocio.cadastros.cadastroCadeira import CadastroCadeira
from negocio.cadastros.cadastroConta import CadastroConta


class ControladorCadastroCadeira(metaclass=SingletonMetaclass):
    def __init__(self, cadastro_cadeira: CadastroCadeira, cadastro_conta: CadastroConta) -> None:
        self.cadastro_cadeira = cadastro_cadeira
        self.cadastro_conta = cadastro_conta

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
        deleted = self.cadastro_cadeira.deletar_cadeira(data.get('id'))
        return deleted
    
    def get_cadeiras_by_professor(self, professor_id):
        cadeiras = self.cadastro_cadeira.get_cadeiras_by_professor(professor_id)
        return cadeiras