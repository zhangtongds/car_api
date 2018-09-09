import requests
import json

# tests 

data = requests.get('http://0.0.0.0:5000/vehicles/1689')

security = requests.get('http://0.0.0.0:5000/vehicles/gfafda/doors').json()

fuel = requests.get('http://0.0.0.0:5000/vehicles/adfa/fuel').json()

battery = requests.get('http://0.0.0.0:5000/vehicles/yutgygh/battery').json()


data = json.dumps({
        "action": "fdajkfja"
        })
engine = requests.post('http://0.0.0.0:5000/vehicles/1234/engine', data=data).json()
print(engine)