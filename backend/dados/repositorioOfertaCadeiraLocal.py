
from .iRepositorioOfertaCadeira import IRepositorioOfertaCadeira
from entidades import OfertaCadeira
from sqlalchemy.orm import joinedload


class RepositorioOfertaCadeiraLocal(IRepositorioOfertaCadeira):
    def __init__(self):
        self._cadeiras = []
        self._count = len(self._cadeiras) + 1

    def create(self, data):
        cadeira = OfertaCadeira(**data)
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

    def get_by_professor(self, professor_id):
        for i, item in enumerate(self._cadeiras):
            if item.professor_id == professor_id:
                return self._cadeiras[i]
        # TODO Levantar erro de objeto não encontrado
        return False
        
    def get_by_periodo(self, periodo):
        for i, item in enumerate(self._cadeiras):
            if item.periodo == periodo:
                return self._cadeiras[i]
        # TODO Levantar erro de objeto não encontrado
        return False

