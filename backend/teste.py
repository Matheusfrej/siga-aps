import requests
import json

BASE = "http://127.0.0.1:5000/"

headers = {'Content-Type': 'application/json'}
# data = {'nome': 'Cadeira', 'professor': 1, 'horario': {'seg': 'teste'}, 'centro_universitario': 'CIn'}
data = {'email': 'baws@cin.ufpe.br', 'senha': 123456}
payload = json.dumps(data)
# response = requests.post(BASE + "cadastrar-cadeira", headers=headers, data=payload)
response = requests.post(BASE + "login", headers=headers, data=payload)
print(response.json())