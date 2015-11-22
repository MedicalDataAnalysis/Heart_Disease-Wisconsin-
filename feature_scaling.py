from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
from pandas import DataFrame

df = pd.read_csv("processed_data/cleveland_data_no_missing_value.csv")
for column in df:
    weights = np.array([float(x) for x in df[column]])
    scaler = MinMaxScaler()
    rescaled_weight = scaler.fit_transform(weights)
    df[column] = rescaled_weight

df.to_csv("processed_data/feature_scaled_cleveland_data_no_missing_value.csv",\
            index = False)
