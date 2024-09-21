import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '25ed1cbd3b360b2ffb76178b906a8e3e'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINED_ID = '10522'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : TRAINED_ID})
    assert response.status_code == 200

def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : TRAINED_ID})
    assert response.json()['data'][0]['trainer_name'] == 'Tre'

    