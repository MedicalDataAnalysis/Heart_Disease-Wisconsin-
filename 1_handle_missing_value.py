import pandas as pd
from pandas import DataFrame

def missing_value(df, feature):
    without_missing_value = 0
    total_value = 0
    for patient in range(total_patients):
        if not (df[feature][patient] == '?' or df[feature][patient] == -9):
            without_missing_value += 1
            total_value += float(df[feature][patient])
    number_of_missing_values = total_patients - without_missing_value
    print(feature + ": # of missing value: %d" \
          % number_of_missing_values)
    # Break if no missing values.
    if number_of_missing_values == 0:
        return

    average_to_int = round(total_value / without_missing_value)
    # Assign average value to the missing value.
    for patient in range(total_patients):
        if df[feature][patient] == '?' or df[feature][patient] == -9:
            df.set_value(patient, feature, average_to_int)

df = pd.read_csv("processed_data/processed_hungarian_data.csv")

total_patients = len(df)

features = df.columns
for feature in features:
    missing_value(df, feature)

df.to_csv("processed_data2(no_missing_value)/hungarian.csv", \
            index = False)
