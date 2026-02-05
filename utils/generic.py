import numpy as np
import pandas as pd

def arr_avg(arr):
    return np.average(arr)

def min_max(array):
    mn=array.min()
    mx=array.max()
    return mn,mx
