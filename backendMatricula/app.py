from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from presenters import *

import requests

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(VerHorarioPresenter, '/ver-horario')
api.add_resource(MatriculaPresenter, '/fazer-matricula')
api.add_resource(EditarMatriculaPresenter, '/editar-matricula/<int:matricula_id>')
api.add_resource(DeletarMatriculaPresenter, '/deletar-matricula/<int:matricula_id>')
api.add_resource(GetMatriculaPeriodoPresenter, '/get-matricula/')
api.add_resource(GetMatriculasAlunoPresenter, '/get-matriculas-aluno/')

@app.route('/')
def hello_world():
    hello_response = requests.get('http://cadeiraservice:5001')
    
    # Check if the request was successful
    if hello_response.status_code == 200:
        return f'Greetings from matriculaservice! Response from cadeiraservice: {hello_response.text}'
    else:
        return 'Error connecting to cadeiraservice'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)