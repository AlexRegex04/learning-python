from pprint import pprint as print
import pandas as pd
import numpy as np
from scipy import stats

json = pd.read_json('./test.json')

p = np.percentile(json['speed'], 90)

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39,
        80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

x = np.percentile(ages, 90)

print(x)
