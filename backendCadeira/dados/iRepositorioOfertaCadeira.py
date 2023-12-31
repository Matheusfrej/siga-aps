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
    def get_by_professor_periodo(self, professor_id, periodo):
        pass

    @abstractmethod
    def get_current_by_professor(self, professor_id):
        pass
    
    @abstractmethod
    def get_by_periodo(self):
        pass

    @abstractmethod
    def read_id_in_list(self, id_list):
        pass