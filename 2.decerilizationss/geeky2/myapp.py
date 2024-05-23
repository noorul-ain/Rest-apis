# #---->>>>>>>>>that is cliet application
import requests 
import json
URL = "http://localhost:8000/"

data = {
    "name": "amna",
    "roll": "11",
    "city": "kch"
}

json_data = json.dumps(data)
r = requests.post(URL, data=json_data) 
data = r.json()
print(data)