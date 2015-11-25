import pandas as pd
from pandas import DataFrame

df = pd.read_csv("processed_data2/va.csv")

total_patients = len(df)
for i in range(total_patients):
    if df["num"][i] != 0:
        df.set_value(i, "num", 1)

df.to_csv("processed_data2/va01.csv", index = False)
