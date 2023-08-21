from abc import ABC, abstractmethod

class IRepositorioOfertaCadeira(ABC):
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
    def get_by_professor(self, professor_id):
        pass
    
    @abstractmethod
    def get_by_periodo(self, periodo):
        pass

    @abstractmethod
    def read_id_in_list(self, id_list):
        pass