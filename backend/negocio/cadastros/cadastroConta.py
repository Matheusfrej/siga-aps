from dados import RepositorioContaLocal

class CadastroConta:
    def __init__(self):
        self.repositorio_conta = RepositorioContaLocal()

    def verificaLogin(self, email, senha):
        user = self.repositorio_conta.get_by_email(email)
        return user.senha == senha