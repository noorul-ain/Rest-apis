import requests
import json
URL ='http://localhost:8000/'

def get_data(id = None):
    data = {}
    if id is None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL , data = json_data) #for read get
    # data = r.json()
    print(data)
get_data()


# post for funcation
def post_data():
    data = {
        'name': 'ali',
        'roll': 123,
        'city': 'Bangalore'
    }
    # to convert json data 
    json_data = json.dumps(data)
    r = requests.post(url=URL, data = json_data)#create post
    # data = r.json()
# post_data()

 
# update function
def update_data():
    data = {
        'id':5,
        'name': 'arslan',
        'roll': 56,
        'city': 'lhr'
    }
    # to convert json data 
    json_data = json.dumps(data)
    r = requests.put(url=URL, data = json_data)#update
    # data = r.json()
# update_data()
    

# delete function
def delete_data():
    data = {
        'id':5,
        
    }
    # to convert json data 
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data = json_data)#update
    # data = r.json()
# delete_data()
 
 