# from pprint import pprint as print
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pylab as plt
from sklearn import linear_model

print(linear_model)
csv = pd.read_csv('./data.csv')

x = np.array(csv[["Weight", "Volume"]])
y = np.array(csv['CO2'])
print(y)
# print(np.array(csv[["Weight", "Volume"]]).shape)
