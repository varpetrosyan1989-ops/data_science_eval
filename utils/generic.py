import numpy as np
import pandas as pd

def arr_avg(arr):
    return np.average(arr)

def min_max(arr):
    mn=arr.min()
    mx=arr.max()
    return mn,mx
def get_column(file_path, col_name):
    df = pd.read_csv(file_path)
    return df(col_name)

result = get_column('/content/sample_data/world_university_survey_dataset.csv', 'age')
print(result)
print(arr_avg(result))
print(min_max(result))