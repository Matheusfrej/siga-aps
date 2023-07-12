from dados.iRepositorioConta import IRepositorioConta
from negocio.entidades.conta import ContaAluno

from datetime import date

class RepositorioContaLocal(IRepositorioConta):
    def __init__(self):
        self.contas = [ContaAluno('Ciência da Computação', 1, 'fgm3@cin.ufpe.br', '09265297492', 'Filipe Gomes de Melo', date(2002, 2, 28), '2020.1', 'senha123*')]

    def get_by_email(self, email):
        return list(filter(lambda x: x.email == email, self.contas))[0]