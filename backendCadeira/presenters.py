
from flask_restful import Resource
from flask import request

import traceback

from utils.errors import CamposVaziosError
from utils import CadeiraSerializer, OfertaCadeiraSerializer
from utils import ConflitoDeHorarioError

from app import *

from negocio.controladores import ControladorCadastroCadeira, ControladorOfertaCadeira

from dotenv import load_dotenv
import os

from dados import SQLAlchemyRepositorioFactory, ListRepositorioFactory

from negocio.cadastros import CadastroCadeira, CadastroOfertaCadeira

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
    def validar_cadeira(self, data):
        campos_vazios = []
        campos_obg = ['nome']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)
        else:
            return True

    def post(self):
        try:
            data = request.get_json()
            try:
                self.validar_cadeira(data)
            except:
                return 'Erro interno do servidor', 500
            result = controlador_cadastrar_cadeira.cadastrar_cadeira(data)
            if result:
                return CadeiraSerializer(result).get_data()
            else:
                return {'Error': 'Erro ao cadastrar a cadeira'}, 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500


class EditarCadeiraPresenter(Resource):
    def validar_cadeira(self, data):
        campos_vazios = []
        campos_obg = ['nome']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)
        else:
            return True
    
    def put(self):
        try:
            data = request.get_json()
            try:
                self.validar_cadeira(data)
            except:
                return 'Erro interno do servidor', 500
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
    def validar_oferta_cadeira(self,data):
        campos_vazios = []
        campos_obg = ['centro_universitario', 'professor', 'periodo', 'horario']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)

    def post(self):
        try:
            data = request.get_json()
            try:
                self.validar_oferta_cadeira(data)
            except:
                return 'Erro interno do servidor', 500
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
    def validar_oferta_cadeira(self,data):
        campos_vazios = []
        campos_obg = ['centro_universitario', 'professor', 'periodo', 'horario']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)
    
    def put(self):
        try:
            data = request.get_json()
            try:
                self.validar_oferta_cadeira(data)
            except:
                return 'Erro interno do servidor', 500
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


class GetOfertaCadeiraById(Resource):
    def get(self, oferta_id):
        try:
            result = controlador_oferta_cadeira.get_oferta_cadeira_by_id(oferta_id)
            print(result)
            if result:
                return OfertaCadeiraSerializer(result).get_data()
            elif result == []:
                return result
            else:
                return {'Error': 'Erro ao ler as cadeiras'}, 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500


class GetOfertaCadeiraListById(Resource):
    def get(self):
        try:
            ids = request.args.getlist('ids')
            result = controlador_oferta_cadeira.get_oferta_cadeira_list_by_id(ids)
            print(result)
            if result:
                return OfertaCadeiraSerializer(result, many=True).get_data()
            elif result == []:
                return result
            else:
                return {'Error': 'Erro ao ler as cadeiras'}, 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500