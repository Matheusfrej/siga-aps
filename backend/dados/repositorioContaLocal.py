from dados.iRepositorioConta import IRepositorioConta
from entidades import ContaBase, ContaAluno, ContaProfessor

from datetime import date

class RepositorioContaLocal(IRepositorioConta):
    def __init__(self):
        conta_base_inicial = ContaBase('fgm3@cin.ufpe.br', '09265297492', 'Filipe Gomes de Melo', date(2002, 2, 28), '2020.1', 'senha123*')
        self._contas = [conta_base_inicial]
        self._count = len(self._contas) + 1

    def create(self, data):
        nova_conta = ContaBase(**data)
        self._contas.append(nova_conta)
        self._count += 1
        return nova_conta

    def create_aluno(self, data):
        nova_conta = ContaAluno(**data)
        self._contas.append(nova_conta)
        self._count += 1
        return nova_conta

    def create_professor(self, data):
        nova_conta = ContaProfessor(**data)
        self._contas.append(nova_conta)
        self._count += 1
        return nova_conta

    def read(self, id):
        for item in self.data:
            if item.id == id:
                return item
        return None

    def update(self, id, data):
        for conta in self._contas:
            if conta.id == id:
                for key, value in data.items():
                    setattr(conta, key, value)
                return True
        # TODO Levantar erro de objeto não encontrado
        return False

    def delete(self, id):
        for i, item in enumerate(self._contas):
            if item.id == id:
                del self.data[i]
                return True
        # TODO Levantar erro de objeto não encontrado
        return False

    def get_by_email(self, email):
        for item in self._contas:
            if item.email == email:
                return item
        return None