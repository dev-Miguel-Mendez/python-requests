import requests
import json

url: str = "https://pokeapi.co/api/v2/pokemon/pikachu"







response: requests.Response = requests.get(url)

pokemon_data = response.json()


print(json.dumps(pokemon_data, indent=2)) #$ To Parse a response in the console import json and use json.dumps on a Dict.