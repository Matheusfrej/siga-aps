from abc import ABC, abstractmethod


class IRepositorioMatricula(ABC):
    @abstractmethod
    def create(self, data):
        pass
    
    @abstractmethod
    def get_by_id(self, id):
        pass
    
    @abstractmethod
    def update(self, id, data):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def get_by_aluno(self, id_aluno):
        pass

    @abstractmethod
    def get_current_by_aluno(self, id_aluno):
        pass
