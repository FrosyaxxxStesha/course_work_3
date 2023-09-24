from datetime import datetime
import json
from src import utils
from os.path import join

with open(join("..", "operations.json")) as file:
    py_obj = json.load(file)


def test_drop_json():
    assert utils.drop_json(join("..", "operations.json")) == py_obj


def test_filter_canceled():
    py_lst = utils.filter_canceled(py_obj)
    flag_cancelled = False
    for i in py_lst:
        if i["state"] != "EXECUTED":
            flag_cancelled = True
            break

    assert not flag_cancelled


py_obj = utils.filter_canceled(py_obj)


def test_parse_date():
    for i in py_obj:
        assert utils.parse_date(i) == i["date"]


def test_take_date():
    assert utils.take_date("2017-06-24T10:50:58.294041") == datetime(2017, 6, 24, 10, 50, 58, 294041)


def test_take_operation():
    for i in py_obj:
        assert utils.take_operation(i["date"], py_obj) == i


def test_format_operation():
    for i in py_obj:
        date = i["date"][8:10] + "." + i["date"][5:7] + "." + i["date"][:4]
        try:
            if "Счет" in i["to"]:
                from_op = "Счет " + "**" + i["to"][-4:]
            else:
                from_op = i["to"][:-16] + i["to"][-16: -12] + " " + i["to"][-12:-10] + "** **** " + i["to"][-4:]
        except KeyError:
            from_op = "?"
        if "Счет" in i["to"]:
            to = "Счет " + "**" + i["to"][-4:]
        else:
            to = i["to"][:-16] + i["to"][-16: -12] + " " + i["to"][-12:-10] + "** **** " + i["to"][-4:]
        assert utils.format_operation(i) == (
                                             date,
                                             i["description"],
                                             from_op,
                                             to,
                                             i["operationAmount"]["amount"],
                                             i["operationAmount"]["currency"]["name"]
                                             )
