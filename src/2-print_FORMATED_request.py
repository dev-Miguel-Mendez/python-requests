import json
import requests

url: str = "https://pokeapi.co/api/v2/pokemon/pikachu"



response: requests.Response = requests.get(url)

pokemon_data = response.json()


#$ 1. json.dumps() converts a dict into a string.
#$ 2. indent=n formats the string with n spaces for each line.
print(json.dumps(pokemon_data, indent=4)) 