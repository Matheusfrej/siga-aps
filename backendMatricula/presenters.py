from flask_restful import Resource
from flask import request
from backendMatricula.utils.errors import CamposVaziosError

from negocio.controladores import *
from negocio.cadastros import CadastroMatricula

from utils import AlunoStrategy, MatriculaSerializer

from dados import SQLAlchemyRepositorioFactory, ListRepositorioFactory

from dotenv import load_dotenv

import traceback
import os


load_dotenv('config.env')
db_type = os.getenv('DB_TYPE')
if db_type == 'sqlalchemy':
    repo_factory = SQLAlchemyRepositorioFactory()
else:
    repo_factory = ListRepositorioFactory()

repo_matricula = repo_factory.criar_repositorio_matricula()
cadastro_matricula = CadastroMatricula(repo_matricula)

controladorMatricula = ControladorRealizarMatricula(cadastro_matricula)
controladorVisualizarHorarioCursadas = ControladorVisualizarHorario(
    strategy=AlunoStrategy(cadastro_matricula))


class MatriculaPresenter(Resource):
    def validar_matricula(self, data):
        campos_vazios = []
        campos_obg = ['periodo', 'aluno_id', 'cadeiras']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)

    def post(self):
        data = request.get_json()
        try:
            self.validar_matricula(data)
        except:
            return "Erro interno no servidor", 500
        try:
            result = controladorMatricula.cadastrar_matricula(data)
            return MatriculaSerializer(result).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return e.__str__(), 500


class DeletarMatriculaPresenter(Resource):
    def delete(self, matricula_id):
        return controladorMatricula.deletarMatriculaCadeira(matricula_id)


class EditarMatriculaPresenter(Resource):
    def validar_matricula(self, data):
        campos_vazios = []
        campos_obg = ['periodo', 'aluno_id', 'cadeiras']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)
    
    def put(self, matricula_id):
        data = request.get_json()
        try:
            self.validar_matricula(data)
        except:
            return "Erro interno no servidor", 500
        data['id'] = matricula_id
        return MatriculaSerializer(controladorMatricula.editarMatriculaCadeira(data))


class GetMatriculaPeriodoPresenter(Resource):
    def get(self, aluno_id):
        return MatriculaSerializer(controladorMatricula.getMatriculaCadeira(aluno_id))
    
    
class GetMatriculasAlunoPresenter(Resource):
    def get(self, aluno_id):
        return MatriculaSerializer(controladorMatricula.getMatriculasAluno(aluno_id))


class VerHorarioPresenter(Resource):
    def get(self, aluno_id):
        return controladorVisualizarHorarioCursadas.visualizarHorario(aluno_id)