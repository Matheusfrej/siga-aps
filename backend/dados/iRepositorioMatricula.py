from abc import abstractmethod

class IRepositorioMatricula:
    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_by_aluno(self, id_aluno):
        pass

    @abstractmethod
    def fazer_matricula(self, id):
        pass
