import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "login", {'email': 'fgm3@cin.ufpe.br', 'password': 'testando'})
print(response.json())