import requests
import json

BASE = "http://127.0.0.1:5000/"

headers = {'Content-Type': 'application/json'}
data = {'email': 'fgm3@cin.ufpe.br', 'senha': 123456}
payload = json.dumps(data)
response = requests.post(BASE + "login", headers=headers, data=payload)
token = response.json().get('idToken')
headers = {'Content-Type': 'application/json', 'token': token, 'periodo': '2023.2'}

# data = {'nome': 'Cadeira 5'}
# payload = json.dumps(data)
# response = requests.post(BASE + "cadastrar-cadeira", headers=headers, data=payload)
# print(response.json())

# data = {'horario': {'sex': [15, 16]}, 'centro_universitario': 'CIn', 'professor': 1, 'cadeira': 5, 'periodo': '2023.1'}
# payload = json.dumps(data)
# response = requests.post(BASE + "cadastrar-oferta-cadeira", headers=headers, data=payload)
# print(response.json())

response = requests.get(BASE + "get-cadeiras-periodo", headers=headers)
print(response.json())

payload = json.dumps(data)
response = requests.get(BASE + "ver-horario", headers=headers)
print(response.json())

response = requests.get(BASE + "get-user-info", headers=headers)
print(response.json())