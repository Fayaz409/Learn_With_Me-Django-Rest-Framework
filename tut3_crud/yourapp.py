import requests
import json

url = 'http://127.0.0.1:8000/student-data/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    
    json_data=json.dumps(data)
    
    # Sending the request with params
    r = requests.get(url=url, data=json_data)
    # data=r.json()
    # Print the raw text response
    # print("Raw response content:",data)
    
    try:
        # Attempt to parse the response as JSON
        data = r.json()
        print(data)
    except requests.exceptions.JSONDecodeError as e:
        print("JSON decode error:", e)
# get_data()

def post_data():
    data={
        'name':'Hussain',
        'roll':25,
        'city':'Hydrabad'
        
    }
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data=r.json()
    print(json_data)
    
# post_data()

def update_data():
    data={
        'id':10,
        'name':'Hussain2',
        # 'roll':20,
        'city':'Larkana'
    }
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data)
    data=r.json()
    print(data)

update_data()

def delete_data():
    data={
        'id':9,
    }
    json_data=json.dumps(data)
    r=requests.delete(url=url,data=json_data)
    data=r.json()
    print(data)

   

    
# delete_data()