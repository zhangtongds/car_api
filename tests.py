import requests
import json

# tests 

data = requests.get('http://0.0.0.0:5000/vehicles/1234')

security = requests.get('http://0.0.0.0:5000/vehicles/1234/doors').json()

fuel = requests.get('http://0.0.0.0:5000/vehicles/1234/fuel').json()

battery = requests.get('http://0.0.0.0:5000/vehicles/1234/battery').json()
print(battery)


data = json.dumps({
        "action": "STOP"
        })
engine = requests.post('http://0.0.0.0:5000/vehicles/1234/engine', data=data).json()