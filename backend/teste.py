import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "cadastrar-cadeira", {'nome': 'Cadeira', 'professor': 1, 'horario': {'seg': 'teste'}, 'centro_universitario': 'CIn'})
print(response.json())