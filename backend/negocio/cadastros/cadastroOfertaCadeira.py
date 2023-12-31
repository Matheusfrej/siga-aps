from dados import IRepositorioOfertaCadeira

from utils import CamposVaziosError, ConflitoDeHorarioError, SingletonMetaclass

class CadastroOfertaCadeira(metaclass=SingletonMetaclass):
    def __init__(self, repositorio_oferta_cadeira):
        self.repositorio_oferta_cadeira: IRepositorioOfertaCadeira = repositorio_oferta_cadeira

    def cadastrar_oferta_cadeira(self, data):
        valida = self.validar_oferta_cadeira(data)
        if valida:
            oferta_cadeira = self.repositorio_oferta_cadeira.create(data)
            return oferta_cadeira

    def editar_oferta_cadeira(self, data):
        valida = self.validar_oferta_cadeira(data)
        if valida:
            oferta_cadeira = self.repositorio_oferta_cadeira.update(data)
        return oferta_cadeira
    
    def deletar_oferta_cadeira(self, data):
        deleted = self.repositorio_oferta_cadeira.delete(data)
        return deleted

    def get_ofertas_cadeiras_by_professor(self, professor_id):
        ofertas_cadeiras = self.repositorio_oferta_cadeira.get_by_professor(professor_id)
        return ofertas_cadeiras
    
    def get_ofertas_cadeiras_by_periodo(self, periodo):
        ofertas_cadeiras = self.repositorio_oferta_cadeira.get_by_periodo(periodo)
        return ofertas_cadeiras

    def validar_oferta_cadeira(self, data):
        horario = data['horario']
        cadeiras = self.get_ofertas_cadeiras_by_professor(data['professor'])
        for cadeira in cadeiras:
            for k, v in cadeira.horario.items():
                for h in v:
                    if h in horario.get(k, []):
                        raise ConflitoDeHorarioError(data['nome'], cadeira.nome)
        return True

    def read_id_in_list(self, id_list):
        return self.repositorio_oferta_cadeira.read_id_in_list(id_list)