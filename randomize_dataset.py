import pandas as pd
from pandas import Series, DataFrame
import numpy as np

def randomize():
    af = pd.read_csv("processed_data2(no_missing_value)/all.csv")
    af_fs = pd.read_csv("processed_data3(feature_scaled)/all_fs.csv")
    af_n = pd.read_csv("processed_data4(nominal)/all_n.csv")
    af01 = pd.read_csv("processed_data2(no_missing_value)/all01.csv")
    af01_fs = pd.read_csv("processed_data3(feature_scaled)/all01_fs.csv")
    af01_n = pd.read_csv("processed_data4(nominal)/all01_n.csv")

    rand_af = af.iloc[np.random.permutation(len(af))]
    rand_af_fs = af_fs.iloc[np.random.permutation(len(af_fs))]
    rand_af_n = af_n.iloc[np.random.permutation(len(af_n))]
    rand_af01 = af01.iloc[np.random.permutation(len(af01))]
    rand_af01_fs = af01_fs.iloc[np.random.permutation(len(af01_fs))]
    rand_af01_n = af01_n.iloc[np.random.permutation(len(af01_n))]

    rand_af.to_csv("processed_data5(randomize)/all.csv", index = False)
    rand_af_fs.to_csv("processed_data5(randomize)/all_fs.csv", index = False)
    rand_af_n.to_csv("processed_data5(randomize)/all_n.csv", index = False)
    rand_af01.to_csv("processed_data5(randomize)/all01.csv", index = False)
    rand_af01_fs.to_csv("processed_data5(randomize)/all01_fs.csv", index = False)
    rand_af01_n.to_csv("processed_data5(randomize)/all01_n.csv", index = False)
