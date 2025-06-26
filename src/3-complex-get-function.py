import requests
import typing as t
import json

base_url: str = "https://pokeapi.co/api/v2/pokemon/"




def get_pokemon_info(pokemon_name: str) -> t.Dict[t.Any, t.Any]:

    full_url: str = base_url + pokemon_name 

    print(full_url)

    response: requests.Response = requests.get(full_url)

    if(response.status_code == 200):
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(response.status_code)
        return {'message': 'error'}





info = get_pokemon_info('pikachu') #$ This is a Dict (t.Dict[t.Any, t.Any])

print(info['name']) #$ This is a string

print(json.dumps(info, indent=2))