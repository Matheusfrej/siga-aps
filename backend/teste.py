import requests
import json

BASE = 'http://127.0.0.1:5000/'

headers = {'Content-Type': 'application/json'}
data = {'email': 'fgm3@cin.ufpe.br', 'senha': 123456}
payload = json.dumps(data)
response = requests.post(BASE + 'login', headers=headers, data=payload)
token = response.json().get('idToken')
headers = {'Content-Type': 'application/json', 'token': token}

payload = json.dumps(data)
response = requests.get(BASE + 'ver-horario', headers=headers)
print(response.json())

response = requests.get(BASE + 'get-user-info', headers=headers)
print(response.json())