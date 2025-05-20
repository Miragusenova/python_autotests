import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b5622ccc9e75a2eb9d38c3ea541ba678'
HEADER = { 'Content-Type' : 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '33746'

#ответ на запрос GET /trainers приходит с кодом 200
def test_status_code():
    response = requests.get(url= f'{URL}/trainers', headers = HEADER, params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

#в ответе приходит строчка с именем моего тренера "Дядя Федор"
def test_part_of_response():
    response_get = requests.get(url= f'{URL}/trainers/33746', headers = HEADER, params = {'id': TRAINER_ID})
    assert response_get.json()["trainer_name"]== 'Дядя Федор'

@pytest.mark.parametrize('key,value',[('trainer_name', 'Дядя Федор'),('id', TRAINER_ID)])
def test_parametrize(key,value):
    response_parametrize = requests.get(url= f'{URL}/trainers/33746', headers = HEADER, params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()[key]==value