import requests

def get_pokemon_info(pokemon_id):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            name = data['name']
            ability_name =[ability['ability']['name'] for ability in data['abilities']]
            return name,ability_name
    except BaseException:
        return "Ошибка сервера"
    else:
        return None

if __name__ == '__main__':
    pokemon_id = input("Введите ID покемона: ")
    info = get_pokemon_info(pokemon_id)
    if info:
        name, ability = info
        print(f'Имя покемона:{name}')
        print(f"Способности:{', '.join(ability)}")



