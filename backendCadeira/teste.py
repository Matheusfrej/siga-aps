import requests
import json

BASE = "http://127.0.0.1:5000/"

headers = {'Content-Type': 'application/json'}
data = {'nome': 'Cadeira 5'}
payload = json.dumps(data)
response = requests.post(BASE + "cadastrar-cadeira", headers=headers, data=payload)
cadeira = response.json()
print('A', cadeira)
print()

data = {'nome': 'Cadeira 7', 'id': str(cadeira.get('id')), 'prerequisitos': ['1', '2'], 'corequisitos': ['1', '2'], 'equivalencias': ['1', '2']}
payload = json.dumps(data)
response = requests.put(BASE + "editar-cadeira", headers=headers, data=payload)
cadeira_editada = response.json()
print('B', cadeira_editada)
print()

data = {'cadeira': str(cadeira.get('id')), 'horario': {'sex': [15, 16]}, 'centro_universitario': 'CIn', 'professor': 1, 'periodo': '2023.1'}
payload = json.dumps(data)
response = requests.post(BASE + "cadastrar-oferta-cadeira", headers=headers, data=payload)
oferta_cadeira = response.json()
print('C', oferta_cadeira)
print()

data = {'cadeira': str(cadeira.get('id')), 'horario': {'seg': [15, 16]}, 'centro_universitario': 'CIn 2', 'professor': str(cadeira.get('id')), 'periodo': '2023.2', 'id': str(oferta_cadeira.get('id'))}
payload = json.dumps(data)
response = requests.put(BASE + "editar-oferta-cadeira", headers=headers, data=payload)
cadeira_editada = response.json()
print('D', cadeira_editada)
print()

data = {'professor_id': 23}
payload = json.dumps(data)
response = requests.get(BASE + "get-cadeiras-professor", headers=headers, data=payload)
print(response.json())
print()

data = {'periodo': '2023.1'}
payload = json.dumps(data)
response = requests.get(BASE + "get-cadeiras-periodo", headers=headers, data=payload)
print(response.json())
print()

data = {'id': str(oferta_cadeira.get('id'))}
payload = json.dumps(data)
response = requests.delete(BASE + "deletar-oferta-cadeira", headers=headers, data=payload)
print(response.json())
print()

data = {'id': str(cadeira.get('id'))}
payload = json.dumps(data)
response = requests.delete(BASE + "deletar-cadeira", headers=headers, data=payload)
print(response.json())
print()
