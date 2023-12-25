# from pprint import pprint as print
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pylab as plt
json = pd.read_json('./test.json')
speed = np.array(json['speed'])
age = np.array(json['age'])

# লিনিয়ার রিগ্রেশনের কিছু গুরুত্বপূর্ণ মূল মান প্রদান করে এমন একটি পদ্ধতি চালান:
slope, intercept, r, p, std_err = stats.linregress(age, speed)
# print(stats.linregress(age, speed))
# একটি ফাংশন তৈরি করুন যা একটি নতুন মান ফেরাতে slopeএবং মান ব্যবহার করে। interceptএই নতুন মানটি প্রতিনিধিত্ব করে যেখানে y-অক্ষে সংশ্লিষ্ট x মানটি স্থাপন করা হবে:


def myfunc(x):
    return slope * x + intercept
    # y =  mx + c

# ফাংশনের মাধ্যমে x অ্যারের প্রতিটি মান চালান। এর ফলে y-অক্ষের জন্য নতুন মান সহ একটি নতুন অ্যারে আসবে:


mymodel = list(map(myfunc, age))

# # মূল স্ক্যাটার প্লট আঁকুন:
plt.scatter(x=age, y=speed)
# রৈখিক রিগ্রেশন লাইন আঁকুন:
plt.plot(age, mymodel)


# চিত্রটি প্রদর্শন করুন:
plt.show()
