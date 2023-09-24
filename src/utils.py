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
    pass


def take_operation(date, py_obj):
    pass


def format_operation(py_dict):
    pass



if __name__ == "__main__":
    filter_canceled(drop_json("../operations.json"))
