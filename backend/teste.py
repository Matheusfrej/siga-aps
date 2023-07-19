import requests
import json

BASE = "http://127.0.0.1:5000/"

headers = {'Content-Type': 'application/json'}
data = {'nome': 'Cadeira', 'professor': 1, 'horario': {'seg': 'teste'}, 'centro_universitario': 'CIn'}
payload = json.dumps(data)
response = requests.post(BASE + "cadastrar-cadeira", headers=headers, data=payload)
print(response.json())