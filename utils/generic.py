# Գործիքների հավաքածու՝ մոդուլ

import numpy as np
import pandas as pd


def read_file_pandas(filename, col_name):
    try:
        csv_file_data = pd.read_csv(filename)
        return csv_file_data[col_name]
    except KeyError:
        print("KeyError: Column->", list(csv_file_data.columns), f"Provided -> {col_name}")
        return None
    except FileNotFoundError:
        print("Message-> ")


def arr_avg(arr):
    return np.average(arr)


def min_max(arr):
    mn = arr.min()
    mx = arr.max()
    return mn, mx


def get_column(file_path, col_name):
    df = pd.read_csv(file_path)
    return df(col_name)


def print_column_names(df):
    print("\n Columns of table")
    for col in df.columns:
        print(f" - {col}")


def print_basic_info(df):
    print(df.info())


def analyze_missing_values(df):
    missing_data = df.isnull().sum()
    if missing_data.sum() == 0:
        print("All cells are filled")
    else:
        print(missing_data[missing_data > 0])
