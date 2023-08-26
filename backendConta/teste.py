import requests
import json

BASE_CONTA = "http://localhost:5000/conta/"
BASE_CADEIRA = "http://localhost:5000/cadeira/"

headers = {'Content-Type': 'application/json'}
data = {'email': 'fgm3@cin.ufpe.br', 'senha': 123456}
payload = json.dumps(data)
response = requests.post(BASE_CONTA + "login", headers=headers, data=payload)
token = response.json().get('idToken')
print(token)

headers = {'Content-Type': 'application/json', 'token': token, 'periodo': '2023.2'}
data = {'nome': 'Cadeira 14'}
payload = json.dumps(data)
response = requests.post(BASE_CADEIRA + 'cadastrar-cadeira', headers=headers, data=payload)
cadeira2 = response.json()
print('A', cadeira2)