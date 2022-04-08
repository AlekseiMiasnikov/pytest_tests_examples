import json
from os.path import join
from pathlib import Path
from PIL import Image


def get_settings(environment):
    ROOT_DIR = Path(__file__).parent.parent
    CONFIG_PATH = join(ROOT_DIR, 'config/config.json')
    with open(CONFIG_PATH) as data:
        config = json.load(data)
        return config[environment]


def remove_user(users, user_id, token, id):
    users.delete({
        'id': id,
        'token': token,
        'user_id': user_id,
    })


def create_image(type='png', size=(500, 500), name='test'):
    img = Image.new('RGB', size, 'red')
    img.save(f'{Path(__file__).parent.parent}/data/files/{name}.{type}')
    return f'{Path(__file__).parent.parent}/data/files/{name}.{type}'
