from .. import cli


def append_to_file(file_path, list_of_chars):
    with open(file_path, 'a') as file:
        for char in list_of_chars:
            file.write(char)


def clean_file(file_path):
    with open(file_path, 'w'):
        pass
    cli.message_to_screen('Content removed', True)


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        cli.message_to_screen('File does not exists', False)
