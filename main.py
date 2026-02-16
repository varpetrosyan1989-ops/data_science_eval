# Գործարկման ֆայլ
from utils.generic import arr_avg, min_max, get_column, print_column_names, print_basic_info, analyze_missing_values, read_file_pandas


while True:
    user_input = input("input path: ")
    col_name= input("Input column name")
    result = get_column(user_input, col_name)
    print(result)
    print(arr_avg(result))
    print(min_max(result))
    data = read_file_pandas("user input")
    print_column_names(data)
    print_basic_info(data)
    analyze_missing_values(data)
    if user_input == "break":
        print("Finished")
        break
    else:
        print(f"Your input is {user_input}")

