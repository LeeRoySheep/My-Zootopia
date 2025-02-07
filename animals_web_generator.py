import json

def load_data(data_path):
    """
    function to read json file at :param
    :param data_path:
    :return:
    """
    with open(data_path, 'r') as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
    if "name" in animal:
        print(f'Name: {animal["name"]}')
    if "diet" in animal["characteristics"]:
        print(f'Diet: {animal["characteristics"]["diet"]}')
    if "location" in animal:
        print(f'Location: {animal["location"][0]}')
    if "type" in animal["characteristics"]:
        print(f'Type: {animal["characteristics"]["type"]}')
    print()
