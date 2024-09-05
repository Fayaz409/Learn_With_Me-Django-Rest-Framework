from requests.auth import HTTPBasicAuth
import requests
import json

URL = 'https://localhost/create-student/' # Put your local Host

data = {
    'name': 'Fayaz Ali',
    'roll': 21,
    'city': 'Karachi',
}

json_data = json.dumps(data)


res = requests.post(
    url=URL,
    data=json_data
    )

print(res.status_code)
print(res.json())

