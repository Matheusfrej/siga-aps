from .iCadeiraService import ICadeiraService
import requests
import json

class CadeiraServiceApi(ICadeiraService):
    def __init__(self):
        self.baseUrl = 'http://127.0.0.1:8080/'
    
    def get_ofertas_cadeiras_periodo(self, data):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.baseUrl + "get-cadeiras-periodo", headers=headers)
        return response.json()
    
    def get_oferta_cadeira_by_id(self, data):
        headers = {'Content-Type': 'application/json'}
        query_params = "&ids=".join(data)
        response = requests.get(self.baseUrl + "get-oferta-cadeira-list?ids="+query_params, headers=headers)
        return response.json()