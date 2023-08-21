from flask import jsonify, Response
from utils import SingletonMetaclass

from negocio.controladores import *
from negocio.cadastros import CadastroMatricula

from utils import AlunoStrategy

from utils import CadeiraSerializer, ContaSerializer, OfertaCadeiraSerializer

from utils import ConflitoDeHorarioError, CamposVaziosError

from dados import SQLAlchemyRepositorioFactory, ListRepositorioFactory

from dotenv import load_dotenv

import traceback
import os

class Fachada(metaclass=SingletonMetaclass):
    def __init__(self) -> None:
        load_dotenv('config.env')
        db_type = os.getenv('DB_TYPE')
        if db_type == 'sqlalchemy':
            repo_factory = SQLAlchemyRepositorioFactory()
        else:
            repo_factory = ListRepositorioFactory()
        repo_matricula = repo_factory.criar_repositorio_matricula()
        cadastro_matricula = CadastroMatricula(repo_matricula)
        self.__controladorRealizarMatricula = ControladorRealizarMatricula()
        self.__controladorVisualizarHorarioCursadas = ControladorVisualizarHorario(
            strategy=AlunoStrategy(cadastro_matricula)
        )

    def get_curr_user_decorator(func):
        ''' usar em métodos que precisam do usuário '''
        def wrapper(self, data):
            print('aqui',data)
            token = data.pop('token')
            user_info = self.__subsistemaFirebase.getInfoConta(token=token)
            email = user_info['users'][0]['email']
            data['user'] = self.__controladorConta.get_user_by_email(email=email)
            result = func(self, data)
            return result
        return wrapper

    @get_curr_user_decorator
    def getUserInfo(self, data) -> Response:
        try:
            return ContaSerializer(data['user']).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500
    
    @get_curr_user_decorator
    def getOfertaCadeirasPeriodo(self, data) -> Response:
        try:
            ofertas_cadeiras = self.__controladorOfertaCadeira.get_ofertas_cadeiras_by_periodo(data['periodo'])
            return OfertaCadeiraSerializer(ofertas_cadeiras, many=True).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def realizarMatriculaCadeira(self, data) -> Response:
        try:
            matricula = self.__controladorRealizarMatricula.cadastrar_matricula(data)
            return matricula
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def editarMatriculaCadeira(self, data) -> Response:
        try:
            matricula = self.__controladorRealizarMatricula.editar_matricula(data)
            return matricula
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500
        
    @get_curr_user_decorator
    def deletarMatriculaCadeira(self, data) -> Response:
        try:
            matricula = self.__controladorRealizarMatricula.deletar_matricula(data['id'])
            return matricula
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500
        
    @get_curr_user_decorator
    def getMatriculaCadeira(self, data) -> Response:
        try:
            matricula = self.__controladorRealizarMatricula.get_current_by_aluno(data['periodo'])
            return matricula
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500
        
    @get_curr_user_decorator
    def getMatriculasAluno(self, data) -> Response:
        try:
            matriculas = self.__controladorRealizarMatricula.get_matriculas_aluno(data['aluno_id'])
            return matriculas
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def visualizarHorario(self, data) -> Response:
        try:
            user = data['user']
            horario = self.__controladorVisualizarHorarioCursadas.get_horario(user_id=user.id)
            return horario.data
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

