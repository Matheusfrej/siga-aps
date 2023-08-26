import requests
import json

BASE = 'http://localhost:5000/cadeira/'

headers = {'Content-Type': 'application/json'}
data = {'nome': 'Cadeira 1'}
payload = json.dumps(data)
response = requests.post(BASE + 'cadastrar-cadeira', headers=headers, data=payload)
cadeira1 = response.json()
print('A', cadeira1)
print()

headers = {'Content-Type': 'application/json'}
data = {'nome': 'Cadeira 2', 'equivalencias': [cadeira1.get('id')]}
payload = json.dumps(data)
response = requests.post(BASE + 'cadastrar-cadeira', headers=headers, data=payload)
cadeira2 = response.json()
print('A', cadeira2)
print()

# data = {'nome': 'Cadeira 7', 'id': str(cadeira.get('id')), 'prerequisitos': ['1', '2'], 'corequisitos': ['1', '2'], 'equivalencias': ['1', '2']}
# payload = json.dumps(data)
# response = requests.put(BASE + 'editar-cadeira', headers=headers, data=payload)
# cadeira_editada = response.json()
# print('B', cadeira_editada)
# print()

data = {'cadeira': str(cadeira1.get('id')), 'horario': {'sex': [15, 16]}, 'centro_universitario': 'CIn', 'professor': 1, 'periodo': '2022.2'}
payload = json.dumps(data)
response = requests.post(BASE + 'cadastrar-oferta-cadeira', headers=headers, data=payload)
oferta_cadeira = response.json()
print(oferta_cadeira)
print()

data = {'cadeira': str(cadeira2.get('id')), 'horario': {'sex': [15, 16]}, 'centro_universitario': 'CIn', 'professor': 1, 'periodo': '2023.2'}
payload = json.dumps(data)
response = requests.post(BASE + 'cadastrar-oferta-cadeira', headers=headers, data=payload)
oferta_cadeira = response.json()
print(oferta_cadeira)
print()

# response = requests.get(BASE + f'get-oferta-cadeira/{2}')
# print('D', response.json())
# print()

# data = {'cadeira': str(cadeira.get('id')), 'horario': {'qua': [15, 16]}, 'centro_universitario': 'CIn', 'professor': 2, 'periodo': '2023.1'}
# payload = json.dumps(data)
# response = requests.post(BASE + 'cadastrar-oferta-cadeira', headers=headers, data=payload)
# oferta_cadeira = response.json()
# print(oferta_cadeira)
# print()

# data = {'cadeira': str(cadeira.get('id')), 'horario': {'ter': [15, 16]}, 'centro_universitario': 'CIn', 'professor': 3, 'periodo': '2023.1'}
# payload = json.dumps(data)
# response = requests.post(BASE + 'cadastrar-oferta-cadeira', headers=headers, data=payload)
# oferta_cadeira = response.json()
# print(oferta_cadeira)
# print()

# response = requests.get(BASE + f'get-oferta-cadeira-list?ids={str(cadeira.get("id"))}&ids={str(cadeira.get("id")+1)}')
# print('E', response.json())
# print()

# data = {'cadeira': str(cadeira.get('id')), 'horario': {'seg': [15, 16]}, 'centro_universitario': 'CIn 2', 'professor': str(cadeira.get('id')), 'periodo': '2023.2', 'id': str(oferta_cadeira.get('id'))}
# payload = json.dumps(data)
# response = requests.put(BASE + 'editar-oferta-cadeira', headers=headers, data=payload)
# cadeira_editada = response.json()
# print('F', cadeira_editada)
# print()

# data = {'professor_id': 23}
# payload = json.dumps(data)
# response = requests.get(BASE + 'get-cadeiras-professor', headers=headers, data=payload)
# print(response.json())
# print()

# data = {'periodo': '2023.1'}
# payload = json.dumps(data)
# response = requests.get(BASE + 'get-cadeiras-periodo', headers=headers, data=payload)
# print(response.json())
# print()

# data = {'id': str(oferta_cadeira.get('id'))}
# payload = json.dumps(data)
# response = requests.delete(BASE + 'deletar-oferta-cadeira', headers=headers, data=payload)
# print(response.json())
# print()

# data = {'id': str(cadeira.get('id'))}
# payload = json.dumps(data)
# response = requests.delete(BASE + 'deletar-cadeira', headers=headers, data=payload)
# print(response.json())
# print()
