import pandas as pd
from pandas import DataFrame

''' processed_cleveland_data.csv has following properties.

>>> df.describe()
              age         sex          cp    trestbps        chol         fbs  \
count  303.000000  303.000000  303.000000  303.000000  303.000000  303.000000
mean    54.438944    0.679868    3.158416  131.689769  246.693069    0.148515
std      9.038662    0.467299    0.960126   17.599748   51.776918    0.356198
min     29.000000    0.000000    1.000000   94.000000  126.000000    0.000000
25%     48.000000    0.000000    3.000000  120.000000  211.000000    0.000000
50%     56.000000    1.000000    3.000000  130.000000  241.000000    0.000000
75%     61.000000    1.000000    4.000000  140.000000  275.000000    0.000000
max     77.000000    1.000000    4.000000  200.000000  564.000000    1.000000

          restecg     thalach       exang     oldpeak       slope          ca  \
count  303.000000  303.000000  303.000000  303.000000  303.000000  303.000000
mean     0.990099  149.607261    0.326733    1.039604    1.600660    0.676568
std      0.994971   22.875003    0.469794    1.161075    0.616226    0.931963
min      0.000000   71.000000    0.000000    0.000000    1.000000    0.000000
25%      0.000000  133.500000    0.000000    0.000000    1.000000    0.000000
50%      1.000000  153.000000    0.000000    0.800000    2.000000    0.000000
75%      2.000000  166.000000    1.000000    1.600000    2.000000    1.000000
max      2.000000  202.000000    1.000000    6.200000    3.000000    3.000000

             thal         num
count  303.000000  303.000000
mean     4.735974    0.937294
std      1.933392    1.228536
min      3.000000    0.000000
25%      3.000000    0.000000
50%      3.000000    0.000000
75%      7.000000    2.000000
max      7.000000    4.000000
'''

def scale_to_nominal(dataFrame):
    total_patients = len(dataFrame)

    # age
    for patient in range(total_patients):
        if dataFrame["age"][patient] <= 48:
            dataFrame["age"][patient] = 1
        elif dataFrame["age"][patient] <= 56:
            dataFrame["age"][patient] = 2
        elif dataFrame["age"][patient] <= 61:
            dataFrame["age"][patient] = 3
        else:
            dataFrame["age"][patient] = 4

    # trestbps
    for patient in range(total_patients):
        if dataFrame["trestbps"][patient] <= 120:
            dataFrame["trestbps"][patient] = 1
        elif dataFrame["trestbps"][patient] <= 130:
            dataFrame["trestbps"][patient] = 2
        elif dataFrame["trestbps"][patient] <= 140:
            dataFrame["trestbps"][patient] = 3
        else:
            dataFrame["trestbps"][patient] = 4

    # chol
    for patient in range(total_patients):
        if dataFrame["chol"][patient] <= 211:
            dataFrame["chol"][patient] = 1
        elif dataFrame["chol"][patient] <= 241:
            dataFrame["chol"][patient] = 2
        elif dataFrame["chol"][patient] <= 275:
            dataFrame["chol"][patient] = 3
        else:
            dataFrame["chol"][patient] = 4

    # thalach
    for patient in range(total_patients):
        if dataFrame["thalach"][patient] <= 133.5:
            dataFrame["thalach"][patient] = 1
        elif dataFrame["thalach"][patient] <= 153:
            dataFrame["thalach"][patient] = 2
        elif dataFrame["thalach"][patient] <= 166:
            dataFrame["thalach"][patient] = 3
        else:
            dataFrame["thalach"][patient] = 4

    # oldpeak
    for patient in range(total_patients):
        if dataFrame["oldpeak"][patient] <= 0:
            dataFrame["oldpeak"][patient] = 1
        elif dataFrame["oldpeak"][patient] <= 0.8:
            dataFrame["oldpeak"][patient] = 2
        elif dataFrame["oldpeak"][patient] <= 1.6:
            dataFrame["oldpeak"][patient] = 3
        else:
            dataFrame["oldpeak"][patient] = 4

    return dataFrame

df = pd.read_csv("processed_data/processed_cleveland_data.csv")
df = scale_to_nominal(df)
df.to_csv("processed_data/processed_cleveland_data_nominal.csv")
