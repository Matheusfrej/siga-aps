from dados import IRepositorioMatricula
from utils import CamposVaziosError, ConflitoDeHorarioError, SingletonMetaclass


class CadastroMatricula(metaclass=SingletonMetaclass):
    def __init__(self, repositorio_matricula):
        self.repositorio_matricula: IRepositorioMatricula = repositorio_matricula

    def get_current_by_aluno(self, aluno_id):
        matricula = self.repositorio_matricula.get_current_by_aluno(aluno_id)
        return matricula
    
    def cadastrar_matricula(self, data):
        valida = self.validar_matricula(data)
        if valida:
            matricula = self.repositorio_matricula.create(data)
            return matricula
    
    def atualizar_matricula(self, data):
        valida = self.validar_matricula(data)
        if valida:
            matricula = self.repositorio_matricula.update(data)
            return matricula

    def get_matricula(self, data):
        matricula = self.repositorio_matricula.get_by_id(data)
        return matricula
    
    def deletar_matricula(self, data):
        matricula = self.repositorio_matricula.delete(data)
        return matricula
    
    def get_matriculas_aluno(self, data):
        matriculas = self.repositorio_matricula.get_by_aluno(data)
        return matriculas

    def validar_matricula(self, data):
        campos_vazios = []
        campos_obg = ['periodo', 'aluno', 'cadeiras']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)

        cadeiras = data['cadeiras']
        
        for cadeira in cadeiras:
            cadeiras_aux = cadeiras.copy()
            cadeiras_aux.pop(cadeira.index())
            for c in cadeiras_aux:
                for k, v in c.horario.items():
                    for hora in v:
                        if hora in cadeira.horario.get(k, []):
                            raise ConflitoDeHorarioError(c.nome, cadeira.nome)
        return True