from utils.singleton import SingletonMetaclass

class ControladorLogin(metaclass=SingletonMetaclass):
    def __init__(self, cadastroConta, iSubsistemaFirebase):
        self.__cadastroConta = cadastroConta
        self.__iSubsistemaFirebase = iSubsistemaFirebase

    def efetuarLogin(self, email, senha):
        logado = self.__iSubsistemaFirebase.validarLogin(email, senha)
        if logado:
            return logado["idToken"]
        else:
            return {'error': 'email ou senha inválidos'}, 401