from dados.iRepositorioCadeira import IRepositorioCadeira
from negocio.entidades.conta import ContaProfessor
from negocio.entidades.cadeira import Cadeira

from datetime import date

class RepositorioCadeiraLocal(IRepositorioCadeira):
    def __init__(self):
        self._cadeiras = [Cadeira(id=1, nome="Introdução à Programação", horario={"segunda":"8", "quarta":"10", "sexta": "8"}, centro_universitario="Centro de Informática", professor=1)]
        self._count = len(self._cadeiras) + 1

    def get_by_id(self, id):
        return list(filter(lambda c: c.id==id, self._cadeiras))[0]

    def get_by_professor(self, id_professor):
        return list(filter(lambda c: c.professor==id_professor, self._cadeiras))

    def cadastrar_cadeira(self, nome: str, horario: dict, centro_universitario: str, professor: int, corequisitos=[], equivalencias=[], prerequisitos=[], plano_ensino=''):
        if self.validar_cadeira(
                nome=nome,
                horario=horario,
                centro_universitario=centro_universitario,
                professor=professor,
                corequisitos=corequisitos,
                equivalencias=equivalencias,
                prerequisitos=prerequisitos,
                plano_ensino=plano_ensino
            ):
            nova_cadeira = Cadeira(
                id=self._count,
                nome=nome,
                horario=horario,
                centro_universitario=centro_universitario,
                professor=professor,
                corequisitos=corequisitos,
                equivalencias=equivalencias,
                prerequisitos=prerequisitos,
                plano_ensino=plano_ensino)
            self._cadeiras.append(nova_cadeira)
            self._count += 1
            return nova_cadeira
        else:
            pass

    def validar_cadeira(self, nome: str, horario: dict, centro_universitario: str, professor: int, corequisitos=[], equivalencias=[], prerequisitos=[], plano_ensino=''):
        return True