import requests
import json

URL= 'http://127.0.0.1:8080/student/stucreate/'
data= {
    'name': 'Pankaj',
    'roll': 111,
    'city': 'Phaltan'
}

json_data= json.dumps(data)
print(json_data)
r= requests.post(url=URL, data= json_data)
data= r.json()
print(data)