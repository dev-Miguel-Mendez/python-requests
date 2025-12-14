import requests
import typing as t
import json

url: str = "https://pokeapi.co/api/v2/pokemon/pikachu"




def get_pokemon_info() -> t.Dict[t.Any, t.Any]:


    response: requests.Response = requests.get(url)

    if(response.status_code == 200):
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(response.status_code)
        return {'message': 'error'}





info = get_pokemon_info() #$ This is a Dict (t.Dict[t.Any, t.Any])

print(info['name']) #$ This is a string

print(json.dumps(info, indent=2))