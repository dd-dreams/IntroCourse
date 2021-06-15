import json


def load_json(filename):
    try:
        file = open(filename)
    except FileNotFoundError:
        return False
    config = json.load(file)
    return config
