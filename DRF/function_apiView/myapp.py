import requests
import  json

URL= 'http://127.0.0.1:8000/api/studentApi/'

def get_data(id= None):
    data= {}
    if id is not None:
        data= {'id':id}
    headers= {'content-Type':'application/json'}
    json_data= json.dumps(data)
    r= requests.get(url=URL,data=json_data,headers= headers)
    data= r.json()
    print(data)
    
get_data()

def post_data():
    data={
        'name':'Raksh',
        'roll': 122,
        'city': 'Ranchi'
    }
    headers= {'content-Type':'application/json'}
    json_data= json.dumps(data)
    r= requests.post(url= URL,data= json_data,headers= headers)
    data= r.json()
    print(data)
    
post_data()

def update_data():
    data={
        'id':6,
        'name':'Shiv',
        'roll':106,
        'city': 'Satara'
    }
    json_data= json.dumps(data)
    r= requests.put(url= URL,data= json_data)
    data= r.json()
    print(data)
    
# update_data()

def delete_data():
    data={ 'id':6 }
    json_data= json.dumps(data)
    r= requests.delete(url= URL,data= json_data)
    data= r.json()
    print(data)
    
# delete_data()