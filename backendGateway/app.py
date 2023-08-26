from flask import Flask, request, redirect
from flask import request

from flask_cors import CORS
from flask_restful import Api

import requests
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CADEIRA_SERVICE_URL = 'http://cadeiraservice:5001/'  # Replace with the actual URL of cadeiraservice
MATRICULA_SERVICE_URL = 'http://matriculaservice:5002/'  # Replace with the actual URL of matriculaservice

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

