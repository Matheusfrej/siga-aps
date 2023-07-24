from utils import SingletonMetaclass

class CadastroConta(metaclass=SingletonMetaclass):
    def __init__(self, repositorio_conta):
        self.repositorio_conta = repositorio_conta

    def get_by_email(self, email):
        user = self.repositorio_conta.get_by_email(email)
        return user