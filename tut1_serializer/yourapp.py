import requests

URL1='http://127.0.0.1:8000/all-students/'
URL2='http://127.0.0.1:8000/student-info/2'
res=requests.get(url=URL1)
res2=requests.get(url=URL2)

print('All Data:',res.json())
print('One Data Point:',res2.json())