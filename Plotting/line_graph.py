import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn

df = DataFrame(np.random.randn(10, 4).cumsum(0),
               columns = ['A', 'B', 'C', 'D'],
               index = np.arange(0, 100, 10))

print(df)
df.plot()
