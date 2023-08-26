class ConflitoDeHorarioError(Exception):
    def __init__(self, nova_cadeira, cadeira_conflito):
        self.nova_cadeira = nova_cadeira
        self.cadeira_conflito = cadeira_conflito

    def __str__(self):
        return f'Conflito de Horário: Não foi possível criar {self.nova_cadeira} porque seu horário conflita com {self.cadeira_conflito}.'

class CamposVaziosError(Exception):
    def __init__(self, campos):
        self.campos = campos

    def __str__(self):
        return f'Existem campos não preenchidos: {", ".join(self.campos)}.'

class EmailSenhaInvalidosException(Exception):
    def __str__(self) -> str:
        return f'Email ou senha inválidos'