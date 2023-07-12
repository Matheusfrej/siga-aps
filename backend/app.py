from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from negocio import Fachada
from utils.requestParsers import LoginRequestParser

app = Flask(__name__)
api = Api(app)

fachada: Fachada = Fachada()

class LoginResource(Resource):
    login_parser = LoginRequestParser()
    def post(self):
        args = self.login_parser.parse_args()
        print(args)
        print(args['email'])
        print(args['senha'])
        email = args['email']
        senha = args['senha']
        return fachada.efetuarLogin(email=email, senha=senha)

api.add_resource(LoginResource, '/login')

if __name__ == '__main__':
    app.run(debug=True)