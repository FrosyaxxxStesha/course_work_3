from src import utils


def main():
    py_obj_list = utils.drop_json("operations.json")
    filtered_list = utils.filter_canceled(py_obj_list)
    date_list = []
    date_str_obj_dict = {}

    for py_dict in filtered_list:
        date_string = utils.parse_date(py_dict)
        date_time_obj = utils.take_date(date_string)
        date_list.append(date_time_obj)
        date_str_obj_dict[date_time_obj] = date_string

    sorted_date_list = sorted(date_list, reverse=True)

    for last_date in sorted_date_list[:5]:
        str_last_date = date_str_obj_dict[last_date]
        operation = utils.take_operation(str_last_date, filtered_list)
        op_date, op_descr, op_from, op_to, op_amount, op_cur_name = utils.format_operation(operation)
        print(f"{op_date} {op_descr}\n{op_from} -> {op_to}\n{op_amount} {op_cur_name}\n")
    return 0


if __name__ == "__main__":
    main()
