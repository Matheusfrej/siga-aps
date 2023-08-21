from utils import SingletonMetaclass
from negocio.cadastros.cadastroMatricula import CadastroMatricula

class ControladorRealizarMatricula(metaclass=SingletonMetaclass):
    def __init__(self, cadastro_matricula: CadastroMatricula) -> None:
        self.cadastro_matricula = cadastro_matricula

    def cadastrar_matricula(self, data):
        nova_matricula = self.cadastro_matricula.cadastrar_matricula(data)
        if nova_matricula:
            return nova_matricula
        else:
            return False

    def editar_matricula(self, data):
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