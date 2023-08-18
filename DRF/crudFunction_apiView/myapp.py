import requests
import  json

URL= 'http://127.0.0.1:8080/api/student_api/'

def get_data(id= None):
    data= {}
    if id is not None:
        data= {'id':id}
    headers= {'content-Type':'application/json'}
    json_data= json.dumps(data)
    r= requests.get(url=URL,data=json_data,headers=headers)
    data= r.json()
    print(data)
    
# get_data(1)

def post_data():
    data={
        'name':'Suhani',
        'roll': 102,
        'city': 'Saswad'
    }
    headers= {'content-Type':'application/json'}
    json_data= json.dumps(data)
    r= requests.post(url= URL,data= json_data,headers=headers)
    data= r.json()
    print(data)
    
# post_data()

def update_data():
    data={
        'id':5,
        'name':'Shivani',
        'city': 'Pune'
    }
    headers= {'content-Type':'application/json'}
    json_data= json.dumps(data)
    r= requests.put(url= URL,data= json_data,headers=headers)
    data= r.json()
    print(data)
    
# update_data()

def delete_data():
    data={ 'id':5 }
    headers= {'content-type':'application/json'}
    json_data= json.dumps(data)
    r= requests.delete(url= URL,data= json_data,headers=headers)
    data= r.json()
    print(data)
    
delete_data()