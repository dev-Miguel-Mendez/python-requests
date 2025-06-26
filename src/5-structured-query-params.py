import requests
import typing as t


#* We have to waste to pass query parameters.
#* 1-
data: t.Dict[str, str|int] = {"name":"Miguel", "age":2}

# requests.get('http://localhost:3001/python-api/query-test', params=data)



#* 2- Manually


requests.get('http://localhost:3001/python-api/query-test?name=Miguel&age=2') 