import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn

s = Series(np.random.randn(10).cumsum(), index = np.arange(0, 100, 10))
print(s)
s.plot()
