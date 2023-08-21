from utils import SingletonMetaclass
from negocio.cadastros.cadastroMatricula import CadastroMatricula
from comunicacao.CadeiraServiceApi import CadeiraServiceApi

class ControladorRealizarMatricula(metaclass=SingletonMetaclass):
    def __init__(self, cadastro_matricula: CadastroMatricula) -> None:
        self.cadastro_matricula = cadastro_matricula
        self.cadeira_service = CadeiraServiceApi()

    def cadastrar_matricula(self, data):
        cadeiras_entities = []
        for id in data['cadeiras']:
            cadeira = self.cadeira_service.get_oferta_cadeira_by_id(id)
            cadeiras_entities.append(cadeira)
        data['cadeiras'] = cadeiras_entities
        nova_matricula = self.cadastro_matricula.cadastrar_matricula(data)
        if nova_matricula:
            return nova_matricula
        else:
            return False

    def editar_matricula(self, data):
        cadeiras_entities = []
        for id in data['cadeiras']:
            cadeira = self.cadeira_service.get_oferta_cadeira_by_id(id)
            cadeiras_entities.append(cadeira)
        data['cadeiras'] = cadeiras_entities
        matricula = self.cadastro_matricula.atualizar_matricula(data)
        return matricula

    def deletar_matricula(self, data):
        deleted = self.cadastro_matricula.deletar_matricula(data)
        return deleted
    
    def get_matriculas_aluno(self, aluno_id):
        matriculas = self.cadastro_matricula.get_matriculas_aluno(aluno_id)
        return matriculas
    
    def get_current_by_aluno(self, periodo):
        matricula = self.cadastro_matricula.get_current_by_aluno(periodo)
        return matricula