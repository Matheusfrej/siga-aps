from utils.singleton import SingletonMetaclass

class ControladorLogin(metaclass=SingletonMetaclass):
    def __init__(self, cadastroConta):
        self.__cadastroConta = cadastroConta

    def efetuarLogin(self, email, senha):
        logged = self.__cadastroConta.verificaLogin(email, senha)
        if logged:
            return {'token': 'TOKEN'}
        else:
            return {'error': 'email ou senha inválidos'}, 401