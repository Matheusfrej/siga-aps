from abc import abstractmethod

class IRepositorioConta:
    @abstractmethod
    def get_by_email(self, email):
        pass
