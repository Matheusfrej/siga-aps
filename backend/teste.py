import requests
import json

BASE = "http://127.0.0.1:5000/"

# data = {'nome': 'Cadeira', 'professor': 1, 'horario': {'seg': 'teste'}, 'centro_universitario': 'CIn'}
# response = requests.post(BASE + "cadastrar-cadeira", headers=headers, data=payload)
# print(response.json())
headers = {'Content-Type': 'application/json'}
data = {'email': 'baws@cin.ufpe.br', 'senha': 123456}
payload = json.dumps(data)
response = requests.post(BASE + "login", headers=headers, data=payload)
token = response.json().get('idToken')
print(response.json().get('idToken'))

data = {'token': token}
payload = json.dumps(data)
response = requests.get(BASE + "ver-horario", headers=headers, data=payload)
print(response.json())