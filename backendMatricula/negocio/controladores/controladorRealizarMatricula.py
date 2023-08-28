from utils import SingletonMetaclass, CamposVaziosError, ConflitoDeHorarioError, ConflitoDeEquivalencia, ConflitoDePreRequisito, ConflitoDeCoRequisito, CadeiraJaCursada, MatriculaJaRealizada
from negocio.cadastros.cadastroMatricula import CadastroMatricula
from comunicacao.CadeiraServiceApi import CadeiraServiceApi
from functools import reduce
from datetime import datetime

class ControladorRealizarMatricula(metaclass=SingletonMetaclass):
    def __init__(self, cadastro_matricula: CadastroMatricula) -> None:
        self.cadastro_matricula = cadastro_matricula
        self.cadeira_service = CadeiraServiceApi()

    def cadastrar_matricula(self, data):
        cadeiras_entities = self.cadeira_service.get_oferta_cadeira_by_id(data['cadeiras'])
        curr_date = datetime.now()
        year = curr_date.year
        month = curr_date.month
        periodo = f'{year}.{1 if month <= 6 else 2}'
        data['periodo'] = periodo
        valida = self.validar_matricula(data, cadeiras_entities)
        if valida:
            nova_matricula = self.cadastro_matricula.cadastrar_matricula(data)
            if nova_matricula:
                return nova_matricula
            else:
                return False

    def editar_matricula(self, data):
        cadeiras_entities = self.cadeira_service.get_oferta_cadeira_by_id(data['cadeiras'])
        valida = self.validar_matricula(data, cadeiras_entities)
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
    
    def validar_matricula(self, data, cadeira_entities):
        campos_vazios = []
        campos_obg = ['periodo', 'aluno_id', 'cadeiras']
        # matricula_atual = self.cadastro_matricula.get_current_by_aluno(data['aluno_id']) TODO APAGAR ISSO
        # if matricula_atual:
        #     raise MatriculaJaRealizada()
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)
        

        matriculas_anteriores = self.cadastro_matricula.get_matriculas_aluno(data['aluno_id'])
        ofertas_cadeiras_cursadas = map(lambda x: x.cadeiras, matriculas_anteriores)
        ids_cadeiras_cursadas = reduce(lambda x,y: x+y, ofertas_cadeiras_cursadas, [])
        cadeiras = cadeira_entities
        for cadeira in cadeiras:
            for c in cadeira['cadeira'].get('prerequisitos', []):
                if str(c['id']) not in ids_cadeiras_cursadas:
                    raise ConflitoDePreRequisito(cadeira['cadeira']['nome'])
        
        for cadeira in cadeiras:
            for c in cadeira['cadeira'].get('equivalencias', []):
                if str(c['id']) in ids_cadeiras_cursadas:
                    raise ConflitoDeEquivalencia(cadeira['cadeira']['nome'], c['nome'])
        
        ids_cadeiras_matricular = map(lambda x: x['cadeira']['id'], cadeiras)
        for cadeira in cadeiras:
            for c in cadeira['cadeira'].get('corequisitos', []):
                if str(c['id']) not in ids_cadeiras_matricular:
                    raise ConflitoDeCoRequisito(cadeira['cadeira']['nome'])
                
        for cadeira in cadeiras:
            if str(cadeira['cadeira']['id']) in ids_cadeiras_cursadas:
                raise CadeiraJaCursada(cadeira['cadeira']['nome'])
        
        for cadeira in cadeiras:
            cadeiras_aux = cadeiras.copy()
            cadeiras_aux.pop(cadeiras.index(cadeira))
            for c in cadeiras_aux:
                for k, v in c['horario'].items():
                    for hora in v:
                        if hora in cadeira['horario'].get(k, []):
                            raise ConflitoDeHorarioError(c['cadeira']['nome'], cadeira['cadeira']['nome'])

        return True