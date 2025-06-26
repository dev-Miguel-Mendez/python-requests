import requests

url: str = "https://pokeapi.co/api/v2/pokemon/pikachu"


response: requests.Response = requests.get(url)

print(response) # <Response [200]>