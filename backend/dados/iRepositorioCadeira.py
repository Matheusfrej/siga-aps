from abc import ABC, abstractmethod

class IRepositorioCadeira(ABC):
    @abstractmethod
    def create(self, data):
        pass
    
    @abstractmethod
    def read(self, id):
        pass
    
    @abstractmethod
    def update(self, id, data):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def validar_cadeira(self, data):
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

    @abstractmethod
    def deletar_cadeira(self, id):
        pass

    @abstractmethod
    def editar_cadeira(self, nome: str, horario: dict, centro_universitario: str, professor: int, corequisitos=[], equivalencias=[], prerequisitos=[], plano_ensino=''):
        pass
