from datetime import datetime
from json import load


def filter_canceled(py_obj_list):
    without_canc = []

    for py_dict in py_obj_list:

        try:
            if py_dict["state"] == "EXECUTED":
                without_canc.append(py_dict)

        except KeyError:
            continue

    return without_canc


def drop_json(json_file):
    with open(json_file) as file:
        py_obj = load(file)
    return py_obj


def parse_date(py_obj_dict):
    return py_obj_dict["date"]


def take_date(date_str):
    year = int(date_str[:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])
    hours = int(date_str[11:13])
    minutes = int(date_str[14:16])
    seconds = int(date_str[17:19])
    microseconds = int(date_str[-6:])
    return datetime(year, month, day, hours, minutes, seconds, microseconds)


def take_operation(date, py_obj):
    for operation in py_obj:
        if operation["date"] == date:
            return operation


def format_operation(py_dict):
    pass


if __name__ == "__main__":
    pass
