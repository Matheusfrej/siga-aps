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
        cadeira = self.repositorio_cadeira.update(data)
        return cadeira
    
    def deletar_cadeira(self, data):
        deleted = self.repositorio_cadeira.delete(data)
        return deleted

    def get_cadeiras_by_professor(self, professor_id):
        cadeiras = self.repositorio_cadeira.get_by_professor(professor_id)
        return cadeiras

    def validar_cadeira(self, data):
        horario = data['horario']
        cadeiras = self.get_cadeiras_by_professor(data['professor'])
        for cadeira in cadeiras:
            for k, v in cadeira.horario.items():
                for h in v:
                    if h in horario.get(k, []):
                        raise ConflitoDeHorarioError(data['nome'], cadeira.nome)

        campos_vazios = []
        campos_obg = ["nome", "horario", "centro_universitario", "professor"]
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)
        else:
            return True