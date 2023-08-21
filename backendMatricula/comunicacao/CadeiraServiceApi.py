from .iCadeiraService import ICadeiraService
import requests
import json

class CadeiraServiceApi(ICadeiraService):
    def __init__(self):
        self.baseUrl = "http://127.0.0.1:5000/"
    
    def get_ofertas_cadeiras_periodo(self, data): #precisa de token?
        headers = {'Content-Type': 'application/json', 'periodo': data}
        response = requests.get(self.baseUrl + "get-cadeiras-periodo", headers=headers)
        return response.json()
    
    def get_oferta_cadeira_by_id(self, data):
        headers = {'Content-Type': 'application/json', 'id': data}
        response = requests.get(self.baseUrl + "get-oferta-cadeira", headers=headers)
        return response.json()