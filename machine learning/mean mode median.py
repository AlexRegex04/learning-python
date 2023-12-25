from pprint import pprint as print
import pandas as pd
import numpy as np
from scipy import stats

json = pd.read_json('./test.json')
speed = np.array(json['speed'])
# print(np.median(speed))
# print(np.median(np.array([77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103
#                           ])))

# print(stats.mode(speed).mode[0])
