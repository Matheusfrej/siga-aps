from dados.iRepositorioCadeira import IRepositorioCadeira

from utils import CamposVaziosError, ConflitoDeHorarioError, SingletonMetaclass

class CadastroCadeira(metaclass=SingletonMetaclass):
    def __init__(self, repositorio_cadeira):
        self.repositorio_cadeira: IRepositorioCadeira = repositorio_cadeira

    def cadastrar_cadeira(self, data):
        cadeira = self.repositorio_cadeira.create(data)
        return cadeira

    def editar_cadeira(self, data):
        cadeira_id = data.pop('id', None)
        cadeira = self.repositorio_cadeira.update(cadeira_id, data)
        return cadeira
    
    def deletar_cadeira(self, data):
        deleted = self.repositorio_cadeira.delete(data)
        return deleted

    def read_id_in_list(self, id_list):
        return self.repositorio_cadeira.read_id_in_list(id_list)

    def get_all_cadeiras(self):
        return self.repositorio_cadeira.get_all()
