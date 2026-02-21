# Գործարկման ֆայլ
from utils.generic import (arr_avg, min_max, print_column_names,
                           print_basic_info, analyze_missing_values,
                           read_file_pandas, get_column_from_csv)

while True:
    user_input = input("input path: ")
    col_name = input("Input column name")
    result = get_column_from_csv(user_input, col_name)
    print(result)
    print(arr_avg(result))
    print(min_max(result))
    data = read_file_pandas("user input")
    print(print_column_names(data))
    print(print_basic_info(data))
    print(analyze_missing_values(data))

    if user_input == "break":
        print("Finish")
        break
