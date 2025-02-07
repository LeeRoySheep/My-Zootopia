import json

def load_data(data_path):
    """
    function to read json file at :param
    :param data_path:
    :return:
    """
    with open(data_path, 'r') as handle:
        return json.load(handle)


def create_data_string(animal_data):
    """
    function to create a string with selected data from the json file
    :param animal_data:
    :return:
    """
    output = ''
    for animal in animal_data:
        output += '<li class="cards__item">'
        output += f'  <div class="card__title">{animal["name"]}</div>\n'
        output += '  <p class="card__text">'
        if "diet" in animal["characteristics"]:
            output += f'  <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
        if "location" in animal:
            output += f'  <strong>Location:</strong> {animal["location"][0]}<br/>\n'
        if "type" in animal["characteristics"]:
            output += f'  <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'
        output += '  </p>\n'
        output += '</li>\n'
    return output


def html_reader(html_file_path):
    """
    function to read from html file and return input as string
    :param html_file_path:
    :return: html_script_string
    """
    with open(html_file_path, 'r') as handler:
        return handler.read()


def html_writer(html_file_path, new_string):
    """
    function to save a html file at html_file_path with new_string as input
    :param1 html_file_path:
    :param2 new_string:
    :return:
    """
    with open(html_file_path, 'w') as handler:
        handler.write(new_string)


def main():
    """
    main function combining all functionality of this file
    :return:
    """
    text_input = create_data_string(load_data('animals_data.json'))
    html_writer('animals_template.html',html_reader('animals_template.html').replace('__REPLACE_ANIMALS_INFO__',text_input))


if __name__ == '__main__':
    main()