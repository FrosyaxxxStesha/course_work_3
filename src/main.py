from src import utils


def main():
    # получение и фильтрация списка операций
    py_obj_list = utils.drop_json("operations.json")
    filtered_list = utils.filter_canceled(py_obj_list)

    # создание пустых словарей строковых дат и дат в виде
    # объекта datetime, используется для сравнения дат в сортировке
    date_list = []
    date_str_obj_dict = {}

    # запуск цикла получения дат, преобразования их в объект datetime и
    # записи в словарь и список дат
    for py_dict in filtered_list:
        date_string = utils.parse_date(py_dict)
        date_time_obj = utils.take_date(date_string)
        date_list.append(date_time_obj)
        date_str_obj_dict[date_time_obj] = date_string

    # сортировка дат
    sorted_date_list = sorted(date_list, reverse=True)

    # получение последних пяти операций и их форматирование
    for last_date in sorted_date_list[:5]:
        str_last_date = date_str_obj_dict[last_date]
        operation = utils.take_operation(str_last_date, filtered_list)
        op_date, op_descr, op_from, op_to, op_amount, op_cur_name = utils.format_operation(operation)
        # вывод в консоль информации
        print(f"{op_date} {op_descr}\n{op_from} -> {op_to}\n{op_amount} {op_cur_name}\n")

    # возврат 0 в случае отсутствия ошибок
    return 0


if __name__ == "__main__":
    main()
