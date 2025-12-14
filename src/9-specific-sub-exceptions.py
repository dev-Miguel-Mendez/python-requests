
#%  All these are subclasses of requests.exceptions.RequestException


#* Implementing connection error

import requests


try:
    response = requests.get('http://localhost:3001/python-api/get-test')

except requests.exceptions.ConnectionError as e:
    print('Connection error LOGIC here!!')
    print(type(e))






#* Implementing status-based rejection (eg: 404, 500, etc.) 
#% There is no automatic “status-based rejection” unless you opt into it.

try:
    response = requests.get('https://google.com/2131231312312/sdfdsf') #$ Will get a 404 error
    response.raise_for_status() #$ ONLY this will raise a HTTPError if the status code is not 200

except requests.exceptions.HTTPError as e:
    print('Bad status LOGIC here!!')
    print(e.response.status_code)
    print(type(e))





#* Implementing timeout error

try:
    response = requests.get('https://google.com', timeout=0.0001)
except requests.exceptions.Timeout as e:
    print('Timeout LOGIC here!!')
    print(type(e))