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