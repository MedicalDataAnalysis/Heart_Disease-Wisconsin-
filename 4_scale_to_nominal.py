import pandas as pd
from pandas import DataFrame
import numpy as np

def scale_to_nominal(df, feature):
    if feature == "num":
        return
    quantile = np.percentile(df[feature], [25, 50, 75, 100])

    for patient in range(total_patients):
        if df[feature][patient] <= quantile[0]:
            df.set_value(patient, feature, 1)
        elif df[feature][patient] <= quantile[1]:
            df.set_value(patient, feature, 2)
        elif df[feature][patient] <= quantile[2]:
            df.set_value(patient, feature, 3)
        else:
            df.set_value(patient, feature, 4)

df = pd.read_csv("processed_data2(no_missing_value)/all.csv")

total_patients = len(df)
features = df.columns
for feature in features:
    scale_to_nominal(df, feature)

df.to_csv("processed_data4(nominal)/all_n.csv", index = False)
