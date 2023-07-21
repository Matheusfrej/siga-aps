from utils.singleton import SingletonMetaclass

class ControladorConta(metaclass=SingletonMetaclass):
    def __init__(self, cadastroConta, iSubsistemaFirebase):
        self.__cadastroConta = cadastroConta
        self.__iSubsistemaFirebase = iSubsistemaFirebase

    def efetuarLogin(self, email, senha):
        logado = self.__iSubsistemaFirebase.validarLogin(email, senha)
        if logado:
            return logado
        else:
            return {'error': 'email ou senha inválidos'}, 401
    
    def get_user_by_email(self, email):
        user = self.__cadastroConta.get_by_email(email)
        if user:
            return user
        else:
            return {'error': 'usuário não encontrado'}, 404