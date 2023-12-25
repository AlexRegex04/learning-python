# from pprint import pprint as print
import pandas as pd
import numpy as np
from scipy import stats

json = pd.read_json('./test.json')
speed = np.array(json['speed'])

# variance:
# 1st step: find mean
mean = np.mean(speed)

# 2nd step: find deference from mean value:
deference = speed - mean

# 3rd step: find square value:
square = np.power(deference, 2)

# 4th step: The variance is the average number of these squared differences:
# 4. প্রকরণ হল এই বর্গীয় পার্থক্যগুলির গড় সংখ্যা:
mean_variance = np.mean(square)

# shortcut method
print(np.std(speed))
print(np.power(np.std(speed), 2))
print(np.var(speed))
