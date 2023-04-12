import requests
token = 'токен'
base_url = 'https://pokemonbattle.me:9104/'

#создание покемона
response_add_pokemon = requests.post(f'{base_url}pokemons', headers={'trainer_token' : token}, json={
    "name": "Numi",
    "photo": "https://dolnikov.ru/pokemons/albums/669.png"
    })
print(response_add_pokemon.text)

#смена имени покемона
response_change_name = requests.put(f'{base_url}pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": "9136",
    "name": "Minu",
    })
print(response_change_name.text)

#поймать покемона в покебол
response_add_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": "9136"
    })
print(response_add_pokeball.text)


