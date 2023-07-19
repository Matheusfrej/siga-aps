from abc import ABC, abstractmethod


class IRepositorioConta(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def create_aluno(self, data):
        pass

    @abstractmethod
    def create_professor(self, data):
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
    def get_by_email(self, email):
        pass