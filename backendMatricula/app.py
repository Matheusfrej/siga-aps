from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from presenters import *

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(VerHorarioPresenter, '/ver-horario')
api.add_resource(MatriculaPresenter, '/fazer-matricula')
api.add_resource(EditarMatriculaPresenter, '/editar-matricula')
api.add_resource(DeletarMatriculaPresenter, '/deletar-matricula')
api.add_resource(GetMatriculaPeriodoPresenter, '/get-matricula')
api.add_resource(GetMatriculasAlunoPresenter, '/get-matriculas-aluno')

if __name__ == '__main__':
    app.run(debug=True)