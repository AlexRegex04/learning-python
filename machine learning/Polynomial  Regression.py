# from pprint import pprint as print
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pylab as plt
json = pd.read_json('./test.json')
speed = np.array(json['speed'])
age = np.array(json['age'])


mymodel = np.poly1d(np.polyfit(age, speed, 4))
print(mymodel)

myline = np.linspace(1, 22, 10)

plt.scatter(age, speed)
plt.plot(myline, mymodel(myline))
plt.show()
