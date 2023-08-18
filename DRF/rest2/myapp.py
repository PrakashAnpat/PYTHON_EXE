import requests

# URL= 'http://127.0.0.1:8000/student/stuinfo_all/'
URL= 'http://127.0.0.1:8000/student/stuinfo/1'

r= requests.get(url=URL)
print('r=',r)
data= r.json()

print('data=',data)