import requests
import json


url="http://127.0.0.1:8000/student-data/"

def get_data(id=None):
    data={
        # 'id':id
    }
    if id is not None:
        data={
            'id':id
        }
    headers={
        'Content-Type':'application/json'
    }
    json_data=json.dumps(data)
    r = requests.get(url=url,headers=headers,data=json_data)
    
    print(f"Status Code: {r.status_code}")
    # print(f"Response Content: {r.text}")
    
    if r.status_code == 200:
        try:
            data = r.json()
            print('GET')
            print(data)
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print(f"Request failed with status code: {r.status_code}")

# Test the function
# get_data()

def upadte_data():
    data={
        'id':2,
        'name':'Ravi(Updated))',
        # 'roll':26,
        'city':'Ranchi(Updated)',
        # 'roll':104
    }
    headers={
        'Content-Type':'application/json'
    }
    json_data=json.dumps(data)
    r=requests.put(url=url,headers=headers,data=json_data)
    if r.status_code==200:
        try:
            data=r.json()
            print('Update/n')
            print(data)
        except requests.exceptions.JSONDecodeError as e:
            print(f'Error decoding JSON: {e}')
    else:
        print(f'Request failed with status code: {r.status_code}')

# upadte_data()

def delete_data():
    data={
        'id':2
    }
    headers={
        'Content-Type':'application/json'
    }
    json_data=json.dumps(data)
    r=requests.delete(url=url,headers=headers,data=json_data)
    if r.status_code==200:
        try:
            data=r.json()
            print('Delete')
            print(data)
        except requests.exceptions.JSONDecodeError as e:
            print(f'JSON Decode Error {e}')
    else:
        print(f'Status code Error {r.status_code}')

    

delete_data()

# import requests
# import json

# url = "http://127.0.0.1:8000/student-data/"

def create_data():
    # url="http://127.0.0.1:8000/post/"
    data = {
        'name': 'FayazAli4',
        'roll': 30,
        'city': 'Kolach'
    }
    json_data = json.dumps(data)
    
    # Specify the content type as application/json in the headers
    headers = {
        'Content-Type': 'application/json'
    }

    r = requests.post(url=url, data=json_data, headers=headers)
    
    if r.status_code == 200:
        data = r.json()
        print('Create/n')
        print(data)
    else:
        print(f"Request failed with status code: {r.status_code}")

# create_data()


