import requests
import typing as t

data: t.Dict[str, str] = {"name":"Miguel"}

requests.post('http://localhost:3001/python-api/post-test', json=data)