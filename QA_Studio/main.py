import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '25ed1cbd3b360b2ffb76178b906a8e3e'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}

body_generate = {
    "name": "generate",
    "photo_id": -1
}

response = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_generate)
print(response.text)

pokemon_id = response.json()['id']

body_confirm = {
    "pokemon_id": pokemon_id,
    "name": "New name",
    "photo_id": 2
}

body_confirm2 = {
    "pokemon_id": pokemon_id,
}


response_confirm = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_confirm)
print(response_confirm.text)

response_confirm2 = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_confirm2)
print(response_confirm2.text)





