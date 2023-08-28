from .iContaService import IContaService

import requests

class ContaServiceAPI(IContaService):
    def __init__(self):
        self.baseUrl = 'http://contaservice:5003/'

    def get_user_info(self, headers):
        response = requests.get(self.baseUrl + 'get-user-info', headers=headers)
        user = response.json()
        return user
