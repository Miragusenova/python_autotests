import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b5622ccc9e75a2eb9d38c3ea541ba678'
HEADER = { 'Content-Type' : 'application/json', 'trainer_token': TOKEN }

body_registration = {
    "trainer_token": TOKEN,
    "email": "M9217714464@yandex.ru",
    "password": "7765Pikachu"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "generate",
    "photo_id": -1
}
body_name_сhange = {
    "pokemon_id": "260165",
    "name": "Тузик",
    "photo_id": 20
}
body_pokebol = {
    "pokemon_id": "320014"
}


'''response = requests.post(url= f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print (response.text)'''

'''response_confirmatoin = requests.post(url= f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print (response_confirmatoin.text)'''

#Создание покемона (POST /pokemons)
response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)

#Сохраняем id созданного покемона в переменную
pokemon_id = response_create.json()['id']
print (pokemon_id)

#Смена имени покемона (PUT /pokemons)
name_сhange = requests.put(url= f'{URL}/pokemons', headers = HEADER, json = body_name_сhange)
print (name_сhange.text)

#Поймать покемона в покебол (POST /trainers/add_pokeball)
pokebol_pokemon= requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json=body_pokebol)
print (pokebol_pokemon.text)

