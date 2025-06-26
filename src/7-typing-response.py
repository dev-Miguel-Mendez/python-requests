

from typing import TypedDict
import requests


class Person(TypedDict):
    name: str
    age: int


class TestResponse(TypedDict):
    message: str
    success: bool
    data: Person


def do_post() -> TestResponse:
    res = requests.get('http://localhost:3001/python-api/get-test')
    return res.json()


data: TestResponse = do_post()


#$ Now you're going to access these more easily. 
print(data['message'])
print(data['success'])

print(data['data']['name'])
print(data['data']['age'])