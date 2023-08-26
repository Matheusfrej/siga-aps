from .iCadeiraService import ICadeiraService
import requests
from circuitbreaker import circuit
import json

class CadeiraServiceApi(ICadeiraService):
    def __init__(self):
        self.baseUrl = 'http://cadeiraservice:5001/'
    
    @circuit
    def get_ofertas_cadeiras_periodo(self, data):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.baseUrl + "get-cadeiras-periodo", headers=headers)
        return response.json()
    
    @circuit
    def get_oferta_cadeira_by_id(self, data):
        headers = {'Content-Type': 'application/json'}
        query_params = "&ids=".join(data)
        response = requests.get(self.baseUrl + "get-oferta-cadeira-list?ids="+query_params, headers=headers)
        return response.json()