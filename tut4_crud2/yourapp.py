import requests
import json


url="http://127.0.0.1:8000/student-data/"

def get_data(id=None):
    data={
        'id':id
    }
    json_data=json.dumps(data)
    r = requests.get(url=url,data=json_data)
    
    print(f"Status Code: {r.status_code}")
    # print(f"Response Content: {r.text}")
    
    if r.status_code == 200:
        try:
            data = r.json()
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
        'name':'Ravi(updated)',
        'city':'Ranchi(updated)',
        # 'roll':104
    }
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data)
    data=r.json()
    print(data)

# upadte_data()

def delete_data():
    data={
        'id':1
    }
    json_data=json.dumps(data)
    r=requests.delete(url=url,data=json_data)
    data=r.json()
    print(data)
    

delete_data()

def create_data():
    data={
        'name':'Ravi',
        'roll':105,
        'city':'Ranchi'
    }
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data=r.json()
    print(data)

# create_data()

