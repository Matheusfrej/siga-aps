import requests
import json

BASE = "http://localhost:5000/"
BASE_CONTA = BASE + "conta/"
BASE_CADEIRA = BASE + "cadeira/"
BASE_MATRICULA = BASE + "matricula/"

headers = {'Content-Type': 'application/json'}
data = {'email': 'baws@cin.ufpe.br', 'senha': 123456}
payload = json.dumps(data)
response = requests.post(BASE_CONTA + "login", headers=headers, data=payload)
token = response.json().get('idToken')
print(token)

headers = {'Content-Type': 'application/json', 'token': token}

data = {'periodo': '2023.2', 'cadeiras': ['2']}
payload = json.dumps(data)
response = requests.post(BASE_MATRICULA + 'fazer-matricula', headers=headers, data=payload)
print(response.json())

payload = json.dumps(data)
response = requests.get(BASE + 'ver-horario', headers=headers)
cadeira2 = response.json()
print(cadeira2)

response = requests.get(BASE_CADEIRA + 'get-cadeiras', headers=headers)
cadeira2 = response.json()
print(cadeira2)