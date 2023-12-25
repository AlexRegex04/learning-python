import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from numpy import random
# !random এলোমেলো
# * return 10 random number array ()
# print(random.random(10))

#! Generate Random Number
# ?Generate a random integer from 0 to 100:

x = random.randint(100)
# print(x)
x = random.randint(100, size=100)
# print(x)
# 2D array
x = random.randint(100, size=(3, 5))
# print(x)

# ! Generate Random Float
# ?The random module's rand() method returns a random float between 0 and 1. same as random()
# print(random.rand(10))
# ?  3 rows, each row containing 5 random numbers:
x = random.rand(3, 5)
# print(x)
# !Generate Random Number From Array
'''
The choice() method allows you to generate a random value based on an array of values.
'''
x = random.choice([3, 5, 7, 9])
# ?  3 rows, each row containing 5 random numbers:
x = random.choice([3, 5, 7, 9], size=(3, 5))
# !Random Distribution
'''
একটি র্যান্ডম ডিস্ট্রিবিউশন হল এলোমেলো সংখ্যার একটি সেট যা একটি নির্দিষ্ট সম্ভাব্যতা ঘনত্ব ফাংশন অনুসরণ করে ।
 probabilities do not sum to 1 (সমস্ত সম্ভাব্যতা সংখ্যার যোগফল 1 হওয়া উচিত।)
'''
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
# print(x)
#! Random Permutations of Elements
'''
The NumPy Random module provides two methods for this: shuffle() and permutation().
'''
# ?shuffle(): এলোমেলো করার অর্থ হল জায়গার উপাদানগুলির বিন্যাস পরিবর্তন করা। অর্থাৎ অ্যারে নিজেই। পদ্ধতিটি shuffle()মূল অ্যারেতে পরিবর্তন করে।


arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)

# ?permutation(): পদ্ধতিটি একটি পুনরায় সাজানো অ্যারে প্রদান করে (এবং মূল অ্যারে অপরিবর্তিত রাখে) permutation()।

# print(random.permutation(arr))

# sns.histplot(random.random(100000))
# plt.show()
# !Normal (Gaussian) Distribution
'''
এটি অনেক ইভেন্টের সম্ভাব্যতা বন্টনের সাথে খাপ খায়, যেমন। আইকিউ স্কোর, হার্টবিট ইত্যাদি
random.normal()একটি সাধারণ ডেটা বিতরণ পেতে পদ্ধতিটি ব্যবহার করুন ।
এটির তিনটি পরামিতি রয়েছে:
loc- (মানে) যেখানে ঘণ্টার শিখর বিদ্যমান।
scale- (স্ট্যান্ডার্ড ডেভিয়েশন) গ্রাফ ডিস্ট্রিবিউশন কতটা সমতল হওয়া উচিত।
size- ফিরে আসা অ্যারের আকৃতি।
'''
# 2x3 আকারের একটি র্যান্ডম স্বাভাবিক বন্টন তৈরি করুন:
x = random.normal(size=(2, 3))
# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
x = random.normal(loc=1, scale=2, size=(2, 3))

# sns.distplot(random.normal(size=1000), hist=True)
# plt.show()
# !Binomial Distribution
'''
দ্বিপদী বন্টন একটি বিচ্ছিন্ন বন্টন ।
এটি বাইনারি পরিস্থিতির ফলাফল বর্ণনা করে, যেমন একটি মুদ্রা টস, এটি হয় মাথা বা পুচ্ছ হবে।
এটির তিনটি পরামিতি রয়েছে:
n- পরীক্ষার সংখ্যা।
p- প্রতিটি ট্রায়াল হওয়ার সম্ভাবনা (যেমন একটি কয়েন 0.5 প্রতিটি টসের জন্য)।
size- ফিরে আসা অ্যারের আকৃতি।
'''
x = random.binomial(n=2, p=0.5, size=10)
# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
# sns.distplot(random.normal(loc=50, scale=5, size=1000),
#              hist=True, label='normal')
# sns.distplot(random.binomial(n=100, p=0.5, size=1000),
#              hist=True, label='binomial')
# plt.show()
# !Poisson Distribution
'''
পয়সন ডিস্ট্রিবিউশন একটি বিচ্ছিন্ন ডিস্ট্রিবিউশন ।
এটি একটি নির্দিষ্ট সময়ে কতবার একটি ঘটনা ঘটতে পারে তা অনুমান করে। যেমন কেউ যদি দিনে দুবার খায় তাহলে তার তিনবার খাওয়ার সম্ভাবনা কত?
এর দুটি পরামিতি রয়েছে:
lam- উপরের সমস্যার জন্য রেট বা সংঘটনের পরিচিত সংখ্যা যেমন 2।
size- ফিরে আসা অ্যারের আকৃতি।
'''
x = random.poisson(lam=3, size=10)
# sns.distplot(random.poisson(lam=2, size=1000), kde=False)
# plt.show()
# Difference Between Normal and Poisson Distribution
"""সাধারণ বন্টন অবিচ্ছিন্ন যেখানে বিষ বিচ্ছিন্ন।
কিন্তু আমরা দেখতে পাচ্ছি যে একটি বৃহৎ পর্যাপ্ত বিষ বিতরণের জন্য দ্বিপদীর অনুরূপ এটি নির্দিষ্ট std dev এবং গড়ের সাথে স্বাভাবিক বন্টনের অনুরূপ হয়ে যাবে।
"""
# sns.distplot(random.binomial(n=1000, p=0.01, size=1000),
#              hist=False, label='binomial')
# sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
# !Uniform Distribution(সমবন্টন)
'''
সম্ভাব্যতা বর্ণনা করতে ব্যবহৃত হয় যেখানে প্রতিটি ঘটনা ঘটার সমান সম্ভাবনা থাকে। যেমন এলোমেলো সংখ্যার জেনারেশন।
এটির তিনটি পরামিতি রয়েছে:
a- নিম্ন আবদ্ধ - ডিফল্ট 0 .0।
b- উপরের বাউন্ড - ডিফল্ট 1.0।
size- ফিরে আসা অ্যারের আকৃতি।
'''
# একটি 2x3 অভিন্ন বিতরণ নমুনা তৈরি করুন:
# x = random.uniform(size=(2, 3), low=10, high=100)
# print(x)
# !Logistic Distribution
'''
বৃদ্ধি বর্ণনা করতে লজিস্টিক ডিস্ট্রিবিউশন ব্যবহার করা হয়।
লজিস্টিক রিগ্রেশন, নিউরাল নেটওয়ার্ক ইত্যাদিতে মেশিন লার্নিংয়ে ব্যাপকভাবে ব্যবহৃত হয়।
এটির তিনটি পরামিতি রয়েছে:
loc- মানে, শিখর যেখানে. ডিফল্ট 0।
scale- আদর্শ বিচ্যুতি, বিতরণের সমতলতা। ডিফল্ট 1.
size- ফিরে আসা অ্যারের আকৃতি।
'''
# লজিস্টিক ডিস্ট্রিবিউশন থেকে 1 এবং stddev 2.0 এর গড় সহ 2x3 নমুনা আঁকুন:
x = random.logistic(loc=1, size=(100), scale=2)
# sns.distplot(random.logistic(size=1000), hist=False)
# plt.show()
# !Multinomial Distribution
'''
বহুপদ বন্টন হল দ্বিপদ বন্টনের একটি সাধারণীকরণ।
এটি দ্বিপদ থেকে ভিন্ন বহু-নামিক পরিস্থিতির ফলাফল বর্ণনা করে যেখানে দৃশ্যকল্প দুটির মধ্যে একটি হতে হবে। যেমন জনসংখ্যার রক্তের ধরন, ডাইস রোল ফলাফল।
এটির তিনটি পরামিতি রয়েছে:
n- সম্ভাব্য ফলাফলের সংখ্যা (যেমন ডাইস রোলের জন্য 6)।
pvals- ফলাফলের সম্ভাব্যতার তালিকা (যেমন [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] ডাইস রোলের জন্য)।
size- ফিরে আসা অ্যারের আকৃতি।
'''
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
# !Exponential Distribution (সূচকীয় বিতরণ)
'''
পরবর্তী ইভেন্ট পর্যন্ত সময় বর্ণনা করার জন্য সূচকীয় বন্টন ব্যবহার করা হয় যেমন ব্যর্থতা/সফলতা ইত্যাদি।
এর দুটি পরামিতি রয়েছে:
scale- হারের বিপরীত (পয়সন ডিস্ট্রিবিউশনে লাম দেখুন) ডিফল্ট 1.0।
size- ফিরে আসা অ্যারের আকৃতি।
'''
x = random.exponential(scale=2, size=(2, 3))
#! Chi Square Distribution
'''
চি স্কোয়ার বিতরণ অনুমান যাচাই করার জন্য একটি ভিত্তি হিসাবে ব্যবহার করা হয়।
এর দুটি পরামিতি রয়েছে:
df- (স্বাধীনতার ডিগ্রি)।
size- ফিরে আসা অ্যারের আকৃতি।
'''
x = random.chisquare(df=2, size=(2, 3))

# !Rayleigh Distribution
'''
Rayleigh বন্টন সংকেত প্রক্রিয়াকরণ ব্যবহার করা হয়.
এর দুটি পরামিতি রয়েছে:
scale- (মান বিচ্যুতি) ডিফল্ট ডিস্ট্রিবিউশন কতটা সমতল হবে তা নির্ধারণ করে 1.0)।
size- ফিরে আসা অ্যারের আকৃতি।
'''
# !Pareto Distribution
'''
Pareto এর আইন অনুসরণ করে একটি বন্টন অর্থাৎ 80-20 ডিস্ট্রিবিউশন (20% কারণ 80% ফলাফল ঘটায়)।
এটির দুটি পরামিতি রয়েছে:
a- আকৃতির পরামিতি।
size- ফিরে আসা অ্যারের আকৃতি।
'''
# !Zipf Distribution
x = random.zipf(a=2, size=(2, 3))
print(x)
