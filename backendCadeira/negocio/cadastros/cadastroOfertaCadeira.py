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
            oferta_id = data.pop('id', None)
            oferta_cadeira = self.repositorio_oferta_cadeira.update(oferta_id, data)
            return oferta_cadeira
        return None
    
    def deletar_oferta_cadeira(self, id):
        deleted = self.repositorio_oferta_cadeira.delete(id)
        return deleted

    def get_ofertas_cadeiras_by_professor(self, professor_id):
        ofertas_cadeiras = self.repositorio_oferta_cadeira.get_by_professor(professor_id)
        return ofertas_cadeiras

    def get_current_ofertas_by_professor_periodo(self, professor_id):
        ofertas_cadeiras = self.repositorio_oferta_cadeira.get_current_by_professor(professor_id)
        return ofertas_cadeiras
    
    def get_ofertas_cadeiras_by_periodo(self):
        ofertas_cadeiras = self.repositorio_oferta_cadeira.get_by_periodo()
        return ofertas_cadeiras

    def validar_oferta_cadeira(self, data):
        campos_vazios = []
        campos_obg = ['centro_universitario', 'professor_id', 'periodo', 'horario']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)

        horario = data['horario']
        cadeiras = self.get_ofertas_cadeiras_by_professor(data['professor_id'])
        for cadeira in cadeiras:
            for k, v in cadeira.horario.items():
                for h in v:
                    if h in horario.get(k, []):
                        raise ConflitoDeHorarioError(data['cadeira'], cadeira.cadeira_id)
        return True

    def get_oferta_cadeira_by_id(self, id):
        oferta_cadeira = self.repositorio_oferta_cadeira.read(id)
        return oferta_cadeira

    def get_oferta_cadeira_list_by_id(self, id_list):
        oferta_cadeira = list(self.repositorio_oferta_cadeira.read_id_in_list(id_list).values())
        return oferta_cadeira