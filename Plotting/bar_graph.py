import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn

fig, axes = plt.subplots(2, 1)
data = Series(np.random.rand(16), index = list('abcdefghijklmnop'))
print(data)
data.plot(kind = 'bar', ax = axes[0], color = 'g', alpha = 0.7)
data.plot(kind = 'barh', ax = axes[1], color = 'b', alpha = 0.7)
fig.show()
