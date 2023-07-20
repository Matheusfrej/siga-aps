from dados.iRepositorioCadeira import IRepositorioCadeira
from negocio.entidades import Cadeira


class RepositorioCadeiraLocal(IRepositorioCadeira):
    def __init__(self):
        self._cadeiras = [Cadeira(nome="Introdução à Programação", horario={"segunda":"8", "quarta":"10", "sexta": "8"}, centro_universitario="Centro de Informática", professor=1)]
        self._count = len(self._cadeiras) + 1

    def create(self, data):
        print(data)
        cadeira = Cadeira(**data)
        cadeira.id = self._count
        self._count += 1
        self._cadeiras.append(cadeira)
        return cadeira

    def read(self, id):
        for cadeira in self._cadeiras:
            if cadeira.id == id:
                return cadeira
        return None

    def update(self, id, data):
        for cadeira in self._cadeiras:
            if cadeira.id == id:
                for key, value in data.items():
                    setattr(cadeira, key, value)
                return True
        # TODO Levantar erro de objeto não encontrado
        return False

    def delete(self, id):
        for i, item in enumerate(self._cadeiras):
            if item.id == id:
                del self._cadeiras[i]
                return True
        # TODO Levantar erro de objeto não encontrado
        return False

    def validar_cadeira(self, data):
        for cadeira in self._cadeiras:
            if cadeira.nome == data['nome']:
                return False
        return True

    def get_by_professor(self, professor_id):
        found_cadeiras = []
        for cadeira in self._cadeiras:
            if cadeira.professor == professor_id:
                found_cadeiras.append(cadeira)
        return found_cadeiras