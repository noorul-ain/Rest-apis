import requests
import json


URL = 'http://localhost:8000/stu/2'
r = requests.get(url=URL)
data = r.json 
print(data)