import requests
import json

BASE = 'http://localhost:5002/'

headers = {'Content-Type': 'application/json'}
data = {'aluno_id': 1, 'periodo': '2022.2', 'cadeiras': ['1']}
payload = json.dumps(data)
response = requests.post(BASE + 'fazer-matricula', headers=headers, data=payload)
print(response.json())

headers = {'Content-Type': 'application/json'}
data = {'aluno_id': 1, 'periodo': '2022.2', 'cadeiras': ['1']}
payload = json.dumps(data)
response = requests.post(BASE + 'fazer-matricula', headers=headers, data=payload)
print(response.json())

headers = {'Content-Type': 'application/json'}
data = {'aluno_id': 1, 'periodo': '2023.2', 'cadeiras': ['2']}
payload = json.dumps(data)
response = requests.post(BASE + 'fazer-matricula', headers=headers, data=payload)
print(response.json())