from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
from pandas import DataFrame

df = pd.read_csv("processed_data2(no_missing_value)/all.csv")

for column in df:
    if column == "num":
        continue
    weights = np.array([float(x) for x in df[column]])
    scaler = MinMaxScaler()
    rescaled_weight = np.round(scaler.fit_transform(weights), 4)
    df[column] = rescaled_weight

df.to_csv("processed_data3(feature_scaled)/all_fs.csv",\
            index = False)
