from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from negocio import Fachada

app = Flask(__name__)
api = Api(app)

fachada: Fachada = Fachada()

class LoginResource(Resource):
    def post(self):
        args = request.get_json()
        email = args['email']
        senha = args['senha']
        print(email,senha)
        return fachada.efetuarLogin(email=email, senha=senha)


class CadastrarCadeiraResource(Resource):
    def post(self):
        kwargs = request.get_json()
        return fachada.cadastrarCadeira(kwargs)
    
class MatriculaResource(Resource):
    def post(self):
        kwargs = request.get_json()
        return fachada.realizarMatriculaCadeira(kwargs)
    
class VerHorarioResource(Resource):
    def post(self):
        kwargs = request.get_json()
        return fachada.visualizarHorario(kwargs)

api.add_resource(LoginResource, '/login')
api.add_resource(CadastrarCadeiraResource, '/cadastrar-cadeira')
api.add_resource(VerHorarioResource, '/ver-horario')
api.add_resource(MatriculaResource, '/matricula')

if __name__ == '__main__':
    app.run(debug=True)