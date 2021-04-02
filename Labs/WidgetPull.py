import json
import requests


r = requests.get('http://192.168.5.152:3000')
data=r.json()

for widget in data:
    print(f"{widget['name']} is {widget['color']}")