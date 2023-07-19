from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from negocio import Fachada
from utils.requestParsers import LoginRequestParser
from utils.requestParsers import CadastroCadeiraRequestParser

app = Flask(__name__)
api = Api(app)

fachada: Fachada = Fachada()

class LoginResource(Resource):
    req_parser = LoginRequestParser()
    def post(self):
        print('BBBBBBBB')
        args = self.req_parser.parse_args()
        email = args['email']
        senha = args['senha']
        return fachada.efetuarLogin(email=email, senha=senha)


class CadastrarCadeiraResource(Resource):
    req_parser = CadastroCadeiraRequestParser()
    def post(self):
        kwargs = self.req_parser.parse_args()
        print(kwargs)
        return fachada.cadastrarCadeira(**kwargs)

api.add_resource(LoginResource, '/login')
api.add_resource(CadastrarCadeiraResource, '/cadastrar-cadeira')

if __name__ == '__main__':
    app.run(debug=True)