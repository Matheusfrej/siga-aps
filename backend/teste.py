import requests
import json

BASE = "http://127.0.0.1:5000/"

headers = {'Content-Type': 'application/json'}
data = {'email': 'baws@cin.ufpe.br', 'senha': 123456}
payload = json.dumps(data)
response = requests.post(BASE + "login", headers=headers, data=payload)
token = response.json().get('idToken')
headers = {'Content-Type': 'application/json', 'token': token}

data = {'nome': 'Cadeira', 'horario': {'seg': [17, 18]}, 'centro_universitario': 'CIn'}
payload = json.dumps(data)
response = requests.post(BASE + "cadastrar-cadeira", headers=headers, data=payload)
print(response.json())

# data = {'horario': {'sex': [15, 16]}}
# payload = json.dumps(data)
# response = requests.post(BASE + "cadastrar-cadeira", headers=headers, data=payload)
# print(response.json())

# payload = json.dumps(data)
# response = requests.get(BASE + "ver-horario", headers=headers)
# print(response.json())

response = requests.get(BASE + "get-user-info", headers=headers)
print(response.json())