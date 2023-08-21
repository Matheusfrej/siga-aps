from utils import SingletonMetaclass, CamposVaziosError, ConflitoDeHorarioError, ConflitoDeEquivalencia, ConflitoDePreRequisito, ConflitoDeCoRequisito, CadeiraJaCursada
from negocio.cadastros.cadastroMatricula import CadastroMatricula
from comunicacao.CadeiraServiceApi import CadeiraServiceApi
from functools import reduce

class ControladorRealizarMatricula(metaclass=SingletonMetaclass):
    def __init__(self, cadastro_matricula: CadastroMatricula) -> None:
        self.cadastro_matricula = cadastro_matricula
        self.cadeira_service = CadeiraServiceApi()

    def cadastrar_matricula(self, data):
        cadeiras_entities = self.cadeira_service.get_oferta_cadeira_by_id(data['cadeiras'])
        data['cadeiras_entities'] = cadeiras_entities
        valida = self.validar_matricula(data)
        if valida:
            nova_matricula = self.cadastro_matricula.cadastrar_matricula(data)
            if nova_matricula:
                return nova_matricula
            else:
                return False

    def editar_matricula(self, data):
        cadeiras_entities = self.cadeira_service.get_oferta_cadeira_by_id(data['cadeiras'])
        data['cadeiras_entities'] = cadeiras_entities
        valida = self.validar_matricula(data)
        if valida:
            matricula = self.cadastro_matricula.atualizar_matricula(data)
            return matricula

    def deletar_matricula(self, data):
        deleted = self.cadastro_matricula.deletar_matricula(data)
        return deleted
    
    def get_matriculas_aluno(self, aluno_id):
        matriculas = self.cadastro_matricula.get_matriculas_aluno(aluno_id)
        for matricula in matriculas:
            cadeiras_entities = self.cadeira_service.get_oferta_cadeira_by_id(matricula['cadeiras'])
            matricula['cadeiras'] = cadeiras_entities
        return matriculas
    
    def get_current_by_aluno(self, aluno_id):
        matricula = self.cadastro_matricula.get_current_by_aluno(aluno_id)
        cadeiras_entities = self.cadeira_service.get_oferta_cadeira_by_id(matricula['cadeiras'])
        matricula['cadeiras'] = cadeiras_entities
        return matricula
    
    def validar_matricula(self, data):
        campos_vazios = []
        campos_obg = ['periodo', 'aluno', 'cadeiras']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)

        matriculas_anteriores = self.cadastro_matricula.get_matriculas_aluno(data['aluno_id'])
        ofertas_cadeiras_cursadas = map(lambda x: x['cadeiras'], matriculas_anteriores)
        cadeiras_cursadas = reduce(lambda x,y: x+y, map(lambda x: x['cadeira'], ofertas_cadeiras_cursadas), [])
        ids_cadeiras_cursadas = map(lambda x: x['id'], cadeiras_cursadas)
        cadeiras = data['cadeiras_entities']
        
        for cadeira in cadeiras:
            for c in cadeira['cadeira']['prerequisitos']:
                if c['id'] not in ids_cadeiras_cursadas:
                    raise ConflitoDePreRequisito(cadeira['nome'])
        
        for cadeira in cadeiras:
            for c in cadeira['cadeira']['equivalencias']:
                if c['id'] in ids_cadeiras_cursadas:
                    raise ConflitoDeEquivalencia(cadeira['nome'], c['nome'])
        
        ids_cadeiras_matricular = map(lambda x: x['cadeira']['id'], cadeiras)
        for cadeira in cadeiras:
            for c in cadeira['cadeira']['corequisitos']:
                if c['id'] not in ids_cadeiras_matricular:
                    raise ConflitoDeCoRequisito(cadeira['nome'])
                
        for cadeira in cadeiras:
            if cadeira['id'] in ids_cadeiras_cursadas:
                raise CadeiraJaCursada(cadeira['nome'])
        
        for cadeira in cadeiras:
            cadeiras_aux = cadeiras.copy()
            cadeiras_aux.pop(cadeira.index())
            for c in cadeiras_aux:
                for k, v in c['horario'].items():
                    for hora in v:
                        if hora in cadeira['horario'].get(k, []):
                            raise ConflitoDeHorarioError(c['nome'], cadeira['nome'])
        
        
        return True