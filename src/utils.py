from datetime import datetime
from json import load


def filter_canceled(py_obj_list):
    """
    функция, фильтрующая операции по статусу, пропускает пустые словари,
    возвращает отфильтрованный объект python
    """
    without_canc = []

    for py_dict in py_obj_list:

        try:
            if py_dict["state"] == "EXECUTED":
                without_canc.append(py_dict)

        except KeyError:
            continue

    return without_canc


def drop_json(json_file):
    """
    Получает файл json, декодирует его в объект python,
    возвращает объект python
    """
    with open(json_file) as file:
        py_obj = load(file)
    return py_obj


def parse_date(py_obj_dict):
    """
    извлекает дату из переданного словаря и возвращает её
    """
    return py_obj_dict["date"]


def take_date(date_str):
    """
    переводит строку даты в объект datetime
    """
    year = int(date_str[:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])
    hours = int(date_str[11:13])
    minutes = int(date_str[14:16])
    seconds = int(date_str[17:19])
    microseconds = int(date_str[-6:])
    return datetime(year, month, day, hours, minutes, seconds, microseconds)


def take_operation(date, py_obj):
    """
    получает операцию по дате
    """
    for operation in py_obj:
        if operation["date"] == date:
            return operation


def format_operation(py_dict):
    """
    форматирует операцию для дальнейшего выовода,
    возвращает кортеж данных
    """
    date = py_dict["date"][8:10] + "." + py_dict["date"][5:7] + "." + py_dict["date"][:4]
    try:
        if "Счет" in py_dict["from"]:
            from_op = "Счет " + "**" + py_dict["from"][-4:]
        else:
            from_op = py_dict["from"][:-16] + py_dict["from"][-16: -12] + " " + py_dict["from"][-12:-10] + "** **** " \
                      + py_dict["from"][-4:]
    except KeyError:
        from_op = "?"
    if "Счет" in py_dict["to"]:
        to = "Счет " + "**" + py_dict["to"][-4:]
    else:
        to = py_dict["to"][:-16] + py_dict["to"][-16: -12] + " " + py_dict["to"][-12:-10] + "** **** " + \
             py_dict["to"][-4:]
    return (
                                             date,
                                             py_dict["description"],
                                             from_op,
                                             to,
                                             py_dict["operationAmount"]["amount"],
                                             py_dict["operationAmount"]["currency"]["name"]
                                             )
