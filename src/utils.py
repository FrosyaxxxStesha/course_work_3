from datetime import datetime
from json import load


def filter_canceled(py_obj_list):
    pass


def drop_json(json_file):
    with open(json_file) as file:
        py_obj = load(file)
    return py_obj


def parse_date(py_obj_dict):
    pass


def take_date(date_str):
    pass


def take_operation(date, py_obj):
    pass


def format_operation(py_dict):
    pass
