import requests
import json

BASE = "http://localhost:5003/"

headers = {'Content-Type': 'application/json'}
data = {'email': 'fgm3@cin.ufpe.br', 'senha': 123456}
payload = json.dumps(data)
response = requests.post(BASE + "login", headers=headers, data=payload)
token = response.json()
print(token)