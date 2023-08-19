from utils import SingletonMetaclass
from negocio.cadastros.cadastroOfertaCadeira import CadastroOfertaCadeira
from negocio.cadastros.cadastroConta import CadastroConta


class ControladorOfertaCadeira(metaclass=SingletonMetaclass):
    def __init__(self, cadastro_oferta_cadeira: CadastroOfertaCadeira) -> None:
        self.cadastro_oferta_cadeira = cadastro_oferta_cadeira

    def cadastrar_oferta_cadeira(self, data):
        nova_oferta_cadeira = self.cadastro_oferta_cadeira.cadastrar_oferta_cadeira(data)
        if nova_oferta_cadeira:
            return nova_oferta_cadeira
        else:
            return False

    def editar_oferta_cadeira(self, data):
        nova_oferta_cadeira = self.cadastro_oferta_cadeira.editar_oferta_cadeira(data)
        return nova_oferta_cadeira

    def deletar_oferta_cadeira(self, data):
        deleted = self.cadastro_oferta_cadeira.deletar_oferta_cadeira(data)
        return deleted
    
    def get_ofertas_cadeiras_by_professor(self, professor_id):
        ofertas_cadeiras = self.cadastro_oferta_cadeira.get_ofertas_cadeiras_by_professor(professor_id)
        return ofertas_cadeiras