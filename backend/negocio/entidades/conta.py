from datetime import date

class ContaBase:
    def __init__(
            self,
            id: int,
            email: str,
            cpf: str,
            name: str,
            data_nascimento: date,
            ano_entrada: str,
            senha: str) -> None:
        self.id = id
        self.email = email
        self.cpf = cpf
        self.name = name
        self.data_nascimento = data_nascimento
        self.ano_entrada = ano_entrada
        self.senha = senha

    def __repr__(self) -> str:
        return f'<User {self.id}: {self.email}>'


class ContaAluno(ContaBase):
    def __init__(self, curso: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.curso = curso


class ContaProfessor(ContaBase):
    def __init__(self, siape: str, formacao: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.siape = siape
        self.formacao = formacao
