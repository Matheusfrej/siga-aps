from dados.iRepositorioCadeira import IRepositorioCadeira

from utils import CamposVaziosError, ConflitoDeHorarioError, SingletonMetaclass

class CadastroCadeira(metaclass=SingletonMetaclass):
    def __init__(self, repositorio_cadeira):
        self.repositorio_cadeira: IRepositorioCadeira = repositorio_cadeira

    def cadastrar_cadeira(self, data):
        valida = self.validar_cadeira(data)
        if valida:
            cadeira = self.repositorio_cadeira.create(data)
            return cadeira

    def editar_cadeira(self, data):
        valida = self.validar_cadeira(data)
        if valida:
            cadeira_id = data.pop('id', None)
            cadeira = self.repositorio_cadeira.update(cadeira_id, data)
            return cadeira
        return False
    
    def deletar_cadeira(self, data):
        deleted = self.repositorio_cadeira.delete(data)
        return deleted

    def validar_cadeira(self, data):
        campos_vazios = []
        campos_obg = ['nome']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)
        else:
            return True

    def read_id_in_list(self, id_list):
        return self.repositorio_cadeira.read_id_in_list(id_list)