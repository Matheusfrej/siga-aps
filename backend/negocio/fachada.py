from flask import jsonify, Response
from utils.singleton import SingletonMetaclass

from negocio.controladores import *
from entidades import ContaProfessor, ContaAluno
from negocio.cadastros import CadastroConta
from negocio.cadastros import CadastroCadeira
from negocio.cadastros import CadastroMatricula
from subsistemaFirebase.iSubsistemaFirebase import iSubsistemaFirebase

from utils import ProfessorStrategy, AlunoStrategy

from utils import CadeiraSerializer, ContaSerializer

from utils import ConflitoDeHorarioError, CamposVaziosError

import traceback

class Fachada(metaclass=SingletonMetaclass):
    def __init__(self) -> None:
        cadastro_conta = CadastroConta()
        cadastro_cadeira = CadastroCadeira()
        cadastro_matricula = CadastroMatricula()
        subsistemaFirebase = iSubsistemaFirebase()
        self.__subsistemaFirebase = subsistemaFirebase
        self.__controladorConta = ControladorConta(cadastro_conta,subsistemaFirebase)
        self.__controladorCadastroCadeira: ControladorCadastroCadeira = ControladorCadastroCadeira(
            cadastro_cadeira=cadastro_cadeira,
            cadastro_conta=cadastro_conta)
        self.__controladorRealizarMatricula = ControladorRealizarMatricula()
        self.__controladorVisualizarHorarioLecionadas = ControladorVisualizarHorario(
            cadastro_cadeira=cadastro_cadeira,
            cadastro_matricula=cadastro_matricula,
            strategy=ProfessorStrategy
        )
        self.__controladorVisualizarHorarioCursadas = ControladorVisualizarHorario(
            cadastro_cadeira=cadastro_cadeira,
            cadastro_matricula=cadastro_matricula,
            strategy=AlunoStrategy
        )

    def get_curr_user_decorator(func):
        ''' usar em métodos que precisam do usuário '''
        def wrapper(self, data):
            token = data.pop('token')
            user_info = self.__subsistemaFirebase.getInfoConta(token=token)
            email = user_info["users"][0]["email"]
            data['user'] = self.__controladorConta.get_user_by_email(email=email)
            result = func(self, data)
            return result
        return wrapper

    def efetuarLogin(self, email: str, senha: str) -> Response:
        ''' Realiza o login '''
        try:
            data = self.__controladorConta.efetuarLogin(email=email, senha=senha)
            data['user'] = ContaSerializer(self.__controladorConta.get_user_by_email(email=email)).get_data()
            return data
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500
    
    def criarConta(self, email: str, senha: str) -> Response:
        try:
            conta = self.__subsistemaFirebase.criarConta(email=email, senha=senha)
            return conta
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def getUserInfo(self, data) -> Response:
        try:
            # TODO colocar o serializador
            return ContaSerializer(data['user']).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def cadastrarCadeira(self, data) -> Response:
        try:
            data['professor'] = data.pop('user').id
            cadeira = self.__controladorCadastroCadeira.cadastrar_cadeira(data)
            return CadeiraSerializer(cadeira).get_data()
        except CamposVaziosError as e:
            return e.__str__(), 400
        except ConflitoDeHorarioError as e:
            return e.__str__(), 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500
    
    def editarCadeira(self, data) -> Response:
        try:
            data['professor'] = data.pop('user')
            cadeira = self.__controladorCadastroCadeira.editar_cadeira(data)
            return CadeiraSerializer(cadeira).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    def deletarCadeira(self, data) -> Response:
        try:
            deleted = self.__controladorCadastroCadeira.deletar_cadeira(data)
            return {'success': deleted}
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def getCadeirasProfessor(self, data) -> Response:
        try:
            cadeiras = self.__controladorCadastroCadeira.get_cadeiras_by_professor(data['user'].id)
            return CadeiraSerializer(cadeiras, many=True).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    def realizarMatriculaCadeira(self) -> Response:
        try:
            pass
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def visualizarHorario(self, data) -> Response:
        try:
            user = data['user']
            if type(user) is ContaProfessor:
                horario = self.__controladorVisualizarHorarioLecionadas.get_horario(user_id=user.id)
            else:
                horario = self.__controladorVisualizarHorarioCursadas.get_horario(user_id=user.id)
            return horario.data
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

