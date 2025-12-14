import requests

#% There is no implicit “status-based rejection” unless you opt into it.

#% requests.get() only raises exceptions for transport-level failures, NOT for HTTP error status codes.


#% requests.get() raises subclasses of requests.exceptions.RequestException for things like:

#% DNS resolution failure

#% Connection refused

#% Connection timeout








try:
    response = requests.get('http://localhost:3001/python-api/get-test')


# except requests.exceptions.HTTPError as e:
#     print(type(e))
#     print(e.response.status_code)

except requests.exceptions.ConnectionError as e:
    print('Connection error thrown bc of non existing URL!!')
    print(type(e))

except Exception as e:
    print(e)
    print(type(e))

    


#* Implementing status-based rejection

try:
    response = requests.get('https://google.com/2131231312312/sdfdsf') #$ Will get a 404 error
    print(response.status_code)
    response.raise_for_status() #$ ONLY this will raise a HTTPError if the status code is not 200

except requests.exceptions.HTTPError as e:
    print(type(e))