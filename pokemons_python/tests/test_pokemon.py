import requests
import pytest
TOKEN = 'токен'
BASE_URL = 'https://pokemonbattle.me:9104/'

#статус 200 на GET/trainers
def test_status_code():
    response = requests.get(f'{BASE_URL}trainers', headers={'trainer_token' : TOKEN}, json={
        "trainer_id" : "3861"
    })
    assert response.status_code == 200

#строчка с именем тренера
def test_trainer_name():
    response = requests.get(f'{BASE_URL}trainers', params={'trainer_id' : 3861})
    assert response.json()['trainer_name'] == 'confused.eggplant'