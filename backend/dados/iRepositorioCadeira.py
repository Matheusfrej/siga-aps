from abc import abstractmethod

class IRepositorioCadeira:
    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_by_professor(self, professor_id):
        pass

    @abstractmethod
    def cadastrar_cadeira(self, nome: str, horario: dict, centro_universitario: str, professor: int, corequisitos=[], equivalencias=[], prerequisitos=[], plano_ensino=''):
        pass

    @abstractmethod
    def validar_cadeira(self, nome: str, horario: dict, centro_universitario: str, professor: int, corequisitos=[], equivalencias=[], prerequisitos=[], plano_ensino=''):
        pass
