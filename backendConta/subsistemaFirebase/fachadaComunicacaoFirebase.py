import requests
import json
from requests.exceptions import HTTPError
from utils import SingletonMetaclass


class Firebase(metaclass=SingletonMetaclass):
    ''' Firebase Interface '''
    def __init__(self, config):
        self.api_key = config['apiKey']
        self.auth_domain = config['authDomain']
        self.credentials = None
        self.requests = requests.Session()

    def auth(self):
        return Auth(self.api_key, self.requests, self.credentials)

class Auth(metaclass=SingletonMetaclass):
    ''' Authentication Service '''
    def __init__(self, api_key, requests, credentials):
        self.api_key = api_key
        self.requests = requests
        self.credentials = credentials

    def validarLogin(self, email, password):
        request_ref = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={0}'.format(self.api_key)
        headers = {'content-type': 'application/json; charset=UTF-8'}
        data = json.dumps({'email': email, 'password': password, 'returnSecureToken': True})
        request_object = requests.post(request_ref, headers=headers, data=data)
        raise_detailed_error(request_object)
        return request_object.json()

    def infoConta(self, id_token):
        request_ref = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key={0}'.format(self.api_key)
        headers = {'content-type': 'application/json; charset=UTF-8'}
        data = json.dumps({'idToken': id_token})
        request_object = requests.post(request_ref, headers=headers, data=data)
        raise_detailed_error(request_object)
        return request_object.json()

    def criarConta(self, email, password):
        request_ref = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key={0}'.format(self.api_key)
        headers = {'content-type': 'application/json; charset=UTF-8' }
        data = json.dumps({'email': email, 'password': password, 'returnSecureToken': True})
        request_object = requests.post(request_ref, headers=headers, data=data)
        raise_detailed_error(request_object)
        return request_object.json()

def raise_detailed_error(request_object):
    try:
        request_object.raise_for_status()
    except HTTPError as e:
        raise HTTPError(e, request_object.text)