from dados import IRepositorioMatricula
from utils import SingletonMetaclass


class CadastroMatricula(metaclass=SingletonMetaclass):
    def __init__(self, repositorio_matricula):
        self.repositorio_matricula: IRepositorioMatricula = repositorio_matricula

    def get_current_by_aluno(self, aluno_id):
        matricula = self.repositorio_matricula.get_current_by_aluno(aluno_id)
        return matricula
    
    def cadastrar_matricula(self, data):
        matricula = self.repositorio_matricula.create(data)
        return matricula
    
    def atualizar_matricula(self, data):
        matricula = self.repositorio_matricula.update(data['id'], data)
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