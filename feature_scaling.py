from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
from pandas import DataFrame

df = pd.read_csv("processed_data/cleveland_data_no_missing_value.csv")
for column in df:
    if column == "num":
        continue
    weights = np.array([float(x) for x in df[column]])
    scaler = MinMaxScaler()
    rescaled_weight = np.round(scaler.fit_transform(weights), 4)
    df[column] = rescaled_weight

df.to_csv("feature_scaled_data/feature_scaled_cleveland_data_no_missing_value.csv",\
            index = False)
