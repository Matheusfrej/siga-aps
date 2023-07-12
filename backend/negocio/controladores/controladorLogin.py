from utils.singleton import SingletonMetaclass

class ControladorLogin(metaclass=SingletonMetaclass):
    def __init__(self, cadastro_contas):
        self._cadastro_contas = cadastro_contas

    def efetuarLogin(self, email, senha):
        pass