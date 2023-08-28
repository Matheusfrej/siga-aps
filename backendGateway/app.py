from flask import Flask, request, redirect
from flask import request

from flask_cors import CORS
from flask_restful import Api

import requests
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CADEIRA_SERVICE_URL = 'http://cadeiraservice:5001/'
MATRICULA_SERVICE_URL = 'http://matriculaservice:5002/'
CONTA_SERVICE_URL = 'http://contaservice:5003/'

@app.route('/cadeira', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/cadeira/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def cadeira_service(path):
    if request.method == 'GET':
        response = requests.get(CADEIRA_SERVICE_URL + path, data=request.data, headers=request.headers)
    elif request.method == 'POST':
        response = requests.post(CADEIRA_SERVICE_URL + path, data=request.data, headers=request.headers)
    elif request.method == 'PUT':
        response = requests.put(CADEIRA_SERVICE_URL + path, data=request.data, headers=request.headers)
    elif request.method == 'DELETE':
        response = requests.delete(CADEIRA_SERVICE_URL + path, data=request.data, headers=request.headers)
    return response.content, response.status_code

@app.route('/matricula', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/matricula/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def matricula_service(path):
    if request.method == 'GET':
        response = requests.get(MATRICULA_SERVICE_URL + path, data=request.data, headers=request.headers)
    elif request.method == 'POST':
        response = requests.post(MATRICULA_SERVICE_URL + path, data=request.data, headers=request.headers)
    elif request.method == 'PUT':
        response = requests.put(MATRICULA_SERVICE_URL + path, data=request.data, headers=request.headers)
    elif request.method == 'DELETE':
        response = requests.delete(MATRICULA_SERVICE_URL + path, data=request.data, headers=request.headers)
    return response.content, response.status_code

@app.route('/conta', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/conta/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def conta_service(path):
    if request.method == 'GET':
        response = requests.get(CONTA_SERVICE_URL + path, data=request.data, headers=request.headers)
    elif request.method == 'POST':
        response = requests.post(CONTA_SERVICE_URL + path, data=request.data, headers=request.headers)
    elif request.method == 'PUT':
        response = requests.put(CONTA_SERVICE_URL + path, data=request.data, headers=request.headers)
    elif request.method == 'DELETE':
        response = requests.delete(CONTA_SERVICE_URL + path, data=request.data, headers=request.headers)
    return response.content, response.status_code


@app.route('/ver-horario', methods=['GET'])
def horario_presenter():
    response = requests.get(CONTA_SERVICE_URL + 'get-user-info', data=request.data, headers=request.headers)
    if response.status_code == 200:
        user = response.json()
        if user.get('discriminator') == 'conta_professor':
            response = requests.get(CADEIRA_SERVICE_URL + 'ver-horario', data=request.data, headers=request.headers)
        else:
            response = requests.get(MATRICULA_SERVICE_URL + 'ver-horario', data=request.data, headers=request.headers)
        return response.content, response.status_code
    else:
        return response.content, response.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

