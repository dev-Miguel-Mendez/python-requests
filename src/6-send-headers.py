import requests
import typing as t


headers: t.Dict[str, str] = {

    "Content-Type": "application/json",
    "cookie": "MY_COOKIE=123"
}



requests.post('http://localhost:3001/python-api/cookies-test', headers=headers)