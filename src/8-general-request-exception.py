

#% requests.get() only raises exceptions for transport-level failures, NOT for HTTP error status codes.


import requests

#* "requests.exceptions.RequestException" is a G E N E R A L exception, meaning that all other sub-exceptions are derived from this.






try:
    response = requests.get('http://localhost:3001/python-api/get-test') #$ Non existing URL

except requests.exceptions.RequestException as e:
    #$ General exception will be caught 
    print(type(e)) #! ACTUAL EXCEPTION TYPE: <class 'requests.exceptions.ConnectionError'>





#* Implementing status-based rejection (eg: 404, 500, etc.) 

try:
    response = requests.get('https://google.com/2131231312312/sdfdsf') #$ Will get a 404 error
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    #$ General exception will be caught 
    print(type(e)) #! ACTUAL EXCEPTION TYPE: <class 'requests.exceptions.HTTPError'>