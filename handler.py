import os

from utils import write_json_file, read_json_file


def update_booking_data(new_data: dict, path='booking.json'):
    if not (os.path.exists(path) and os.path.isfile(path)):
        write_json_file(path, data=[])

    data = read_json_file(path)
    data.append(new_data)
    write_json_file(path, data)
