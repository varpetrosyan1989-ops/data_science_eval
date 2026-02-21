# Գործիքների հավաքածու՝ մոդուլ
import numpy as np
import pandas as pd


def read_file_pandas(filename):
    try:
        csv_file_data = pd.read_csv(filename)
        return csv_file_data
    except FileNotFoundError:
        print("File not found!")


def arr_avg(arr):
    return np.average(arr)


def min_max(arr):
    mn = arr.min()
    mx = arr.max()
    return mn, mx


def get_column_from_csv(file_path, col_name):
    csv_file_data = None
    try:
        csv_file_data = read_file_pandas(file_path)
        if csv_file_data is None:
            return None
        return csv_file_data[col_name]
    except KeyError:
        print(f"KeyError: Column: {list(csv_file_data.columns)} Provided  {col_name}")
        return None


def print_column_names(df):
    print(f"\n Columns of dataframe are: ", df.columns)


def print_basic_info(df):
    print(df.info())


def analyze_missing_values(df):
    missing_data = df.isnull().sum()
    if missing_data.sum() == 0:
        print("All cells are filled")
    else:
        print("All cells are empty")
