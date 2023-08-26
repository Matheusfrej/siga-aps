class EmailSenhaInvalidosException(Exception):
    def __str__(self):
        return 'Email ou senha inválidos'