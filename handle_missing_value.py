import pandas as pd
from pandas import DataFrame

df = pd.read_csv("processed_data/processed_cleveland_data.csv")

total_patients = len(df)

# Handle Missing Value for ca
def missing_value_ca(df):
    ca_without_missing_value = 0
    total_value_ca = 0
    for patient in range(total_patients):
        if df["ca"][patient] != '?':
            ca_without_missing_value += 1
            total_value_ca += float(df["ca"][patient])

    print("ca_without_missing_value: %d / %d" \
          % (ca_without_missing_value, total_patients))

    average_to_int = round(total_value_ca / ca_without_missing_value)
    # Assign average value to the missing value.
    for patient in range(total_patients):
        if df["ca"][patient] == '?':
            df["ca"][patient] = average_to_int
    return df

# Handle Missing Value for thal
def missing_value_thal(df):
    thal_without_missing_value = 0
    total_value_thal = 0
    for patient in range(total_patients):
        if df["thal"][patient] != '?':
            thal_without_missing_value += 1
            total_value_thal += float(df["thal"][patient])

    print("thal_without_missing_value: %d / %d" \
          % (thal_without_missing_value, total_patients))

    average_to_int = round(total_value_thal / thal_without_missing_value)
    # Assign average value to the missing value.
    for patient in range(total_patients):
        if df["thal"][patient] == '?':
            df["thal"][patient] = average_to_int
    return df

df = missing_value_ca(df)
df = missing_value_thal(df)

df.to_csv("processed_data/cleveland_data_no_missing_value.csv")
