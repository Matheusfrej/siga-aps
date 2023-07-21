from dados import RepositorioContaSQLAlchemy

class CadastroConta:
    def __init__(self):
        self.repositorio_conta = RepositorioContaSQLAlchemy()

    def get_by_email(self, email):
        user = self.repositorio_conta.get_by_email(email)
        return user