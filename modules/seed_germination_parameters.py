import pandas as pd
import numpy as np

def MGT(df): 
    _ni_sum = 0
    _ni_ti_sum = 0
    cols = list(df.columns)
    for ti in range(len(cols)):
        ni = sum(df[cols[ti]])
        _ni_ti_sum += (ni * (ti+1))
        _ni_sum += ni
        
    return _ni_ti_sum / _ni_sum


def GP(df, Nt):
    Ng = sum(df.sum())
    print(f"Ng = {Ng}")
    return (Ng/Nt) * 100

def Z(df):
    _cNi_2_sum = 0
    cols = list(df.columns)
    for i in range(len(cols)):
        ni = sum(df[cols[i]])
        cNi_2 = (ni*(ni-1))/2
        _cNi_2_sum += cNi_2

    all_germinated_seeds = sum(df.sum()) * (sum(df.sum())-1) / 2
    return _cNi_2_sum / all_germinated_seeds
