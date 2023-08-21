from flask import Flask, request
from flask import request

from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from flask_restful import Resource

from negocio.controladores import ControladorCadastroCadeira, ControladorOfertaCadeira

from dotenv import load_dotenv

from dados import SQLAlchemyRepositorioFactory, ListRepositorioFactory

from utils import CadeiraSerializer, OfertaCadeiraSerializer

from negocio.cadastros import CadastroCadeira, CadastroOfertaCadeira

from utils import ConflitoDeHorarioError

import os
import traceback

app = Flask(__name__)
CORS(app)
api = Api(app)

load_dotenv('config.env')
db_type = os.getenv('DB_TYPE')
if db_type == 'sqlalchemy':
    repo_factory = SQLAlchemyRepositorioFactory()
else:
    repo_factory = ListRepositorioFactory()

repo_cadeira = repo_factory.criar_repositorio_cadeira()
repo_oferta_cadeira = repo_factory.criar_repositorio_oferta_cadeira()

cadastro_cadeira = CadastroCadeira(repo_cadeira)
cadastro_oferta_cadeira = CadastroOfertaCadeira(repo_oferta_cadeira)

controlador_cadastrar_cadeira = ControladorCadastroCadeira(cadastro_cadeira)
controlador_oferta_cadeira = ControladorOfertaCadeira(cadastro_oferta_cadeira)

class CadastrarCadeiraPresenter(Resource):
    def post(self):
        try:
            data = request.get_json()
            result = controlador_cadastrar_cadeira.cadastrar_cadeira(data)
            if result:
                return CadeiraSerializer(result).get_data()
            else:
                return {'Error': 'Erro ao cadastrar a cadeira'}, 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

class EditarCadeiraPresenter(Resource):
    def put(self):
        try:
            data = request.get_json()
            result = controlador_cadastrar_cadeira.editar_cadeira(data)
            if result:
                return CadeiraSerializer(result).get_data()
            else:
                return {'Error': 'Erro ao cadastrar a cadeira'}, 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500


class DeletarCadeiraPresenter(Resource):
    def delete(self):
        try:
            data = request.get_json()
            result = controlador_cadastrar_cadeira.deletar_cadeira(data)
            if result:
                return CadeiraSerializer(result).get_data()
            else:
                return {'Error': 'Erro ao deletar a cadeira'}, 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500


class CadastrarOfertaCadeiraPresenter(Resource):
    def post(self):
        try:
            data = request.get_json()
            result = controlador_oferta_cadeira.cadastrar_oferta_cadeira(data)
            if result:
                return OfertaCadeiraSerializer(result).get_data()
            else:
                return {'Error': 'Erro ao cadastrar a cadeira'}, 500
        except ConflitoDeHorarioError as e:
            return e.__str__(), 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500


class EditarOfertaCadeiraPresenter(Resource):
    def put(self):
        try:
            data = request.get_json()
            result = controlador_oferta_cadeira.editar_oferta_cadeira(data)
            if result:
                return OfertaCadeiraSerializer(result).get_data()
            else:
                return {'Error': 'Erro ao editar a cadeira'}, 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500


class DeletarOfertaCadeiraPresenter(Resource):
    def delete(self):
        try:
            data = request.get_json()
            result = controlador_oferta_cadeira.deletar_oferta_cadeira(data)
            if result:
                return OfertaCadeiraSerializer(result).get_data()
            else:
                return {'Error': 'Erro ao deletar a cadeira'}, 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500


class GetOfertasCadeirasProfessorPresenter(Resource):
    def get(self):
        try:
            data = request.get_json()
            result = controlador_oferta_cadeira.get_ofertas_cadeiras_by_professor(data.get('professor_id'))
            if result:
                return OfertaCadeiraSerializer(result, many=True).get_data()
            elif result == []:
                return result
            else:
                return {'Error': 'Erro ao ler as cadeiras'}, 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500
    

class GetOfertasCadeirasPeriodoPresenter(Resource):
    def get(self):
        try:
            data = request.get_json()
            result = controlador_oferta_cadeira.get_ofertas_cadeiras_by_periodo(data.get('periodo'))
            if result:
                return OfertaCadeiraSerializer(result, many=True).get_data()
            elif result == []:
                return result
            else:
                return {'Error': 'Erro ao ler as cadeiras'}, 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500


api.add_resource(CadastrarCadeiraPresenter, '/cadastrar-cadeira')
api.add_resource(EditarCadeiraPresenter, '/editar-cadeira')
api.add_resource(DeletarCadeiraPresenter, '/deletar-cadeira')
api.add_resource(CadastrarOfertaCadeiraPresenter, '/cadastrar-oferta-cadeira')
api.add_resource(EditarOfertaCadeiraPresenter, '/editar-oferta-cadeira')
api.add_resource(DeletarOfertaCadeiraPresenter, '/deletar-oferta-cadeira')
api.add_resource(GetOfertasCadeirasProfessorPresenter, '/get-cadeiras-professor')
api.add_resource(GetOfertasCadeirasPeriodoPresenter, '/get-cadeiras-periodo')

if __name__ == '__main__':
    app.run(debug=True)