from flask_restful import Resource
from flask import request
from backend.utils.errors import CamposVaziosError
from negocio import Fachada

fachada: Fachada = Fachada()


class LoginPresenter(Resource):
    def post(self):
        args = request.get_json()
        email = args['email']
        senha = args['senha']
        return fachada.efetuarLogin(email=email, senha=senha)


class UserInfoPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.getUserInfo(data)


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
        data = request.get_json()
        try:
            self.validar_cadeira(data)
        except:
            return 'Erro interno do servidor', 500
        print("Cadastrar cadeira resource ", data)
        data['token'] = request.headers.get('token')
        return fachada.cadastrarCadeira(data)


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
        data = request.get_json()
        try:
            self.validar_cadeira(data)
        except:
            return 'Erro interno do servidor', 500
        data['token'] = request.headers.get('token')
        return fachada.editarCadeira(data)


class DeletarCadeiraPresenter(Resource):
    def delete(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.deletarCadeira(data)


class CadastrarOfertaCadeiraPresenter(Resource):
    def validar_oferta_cadeira(self, data):
        campos_vazios = []
        campos_obg = ['centro_universitario', 'professor', 'periodo', 'horario']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)

    def post(self):
        data = request.get_json()
        try:
            self.validar_oferta_cadeira(data)
        except:
            return 'Erro interno do servidor', 500
        print("Cadastrar cadeira resource ", data)
        data['token'] = request.headers.get('token')
        return fachada.cadastrarOfertaCadeira(data)


class EditarOfertaCadeiraPresenter(Resource):
    def validar_oferta_cadeira(self, data):
        campos_vazios = []
        campos_obg = ['centro_universitario', 'professor', 'periodo', 'horario']
        for campo in campos_obg:
            if campo not in data.keys():
                campos_vazios.append(campo)
        if campos_vazios:
            raise CamposVaziosError(campos_vazios)
    
    def put(self):
        data = request.get_json()
        try:
            self.validar_oferta_cadeira(data)
        except:
            return 'Erro interno do servidor', 500
        data['token'] = request.headers.get('token')
        return fachada.editarOfertaCadeira(data)


class DeletarOfertaCadeiraPresenter(Resource):
    def delete(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.deletarOfertaCadeira(data)


class GetOfertasCadeirasProfessorPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.getOfertaCadeirasProfessor(data)
    

class GetOfertasCadeirasPeriodoPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token'),
            'periodo': request.headers.get('periodo')
        }
        return fachada.getOfertaCadeirasPeriodo(data)


class MatriculaPresenter(Resource):
    def post(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.realizarMatriculaCadeira(data)


class VerHorarioPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.visualizarHorario(data)