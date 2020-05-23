import json


def write_json_file(path, data, indent=4):
    with open(path, 'w') as fd:
        json.dump(data, fd, indent=indent)


def read_json_file(path):
    with open(path, 'r') as fd:
        return json.load(fd)
