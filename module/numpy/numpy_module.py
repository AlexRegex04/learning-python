import numpy as np

# ! See version
# print(np.__version__)

# ! Creating arrays
x = np.array(range(100))
# print(x)

# print(type(x))  # ! <class 'numpy.ndarray'>

# ? Check Number of Dimensions?

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ], [
        [1, 2, 3],
        [4, 5, 6]
    ]
])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# !Higher Dimensional Arrays
# ?An array can have any number of dimensions.

x = np.array(list(range(12)), ndmin=3)
# print(x)
# ! NumPy Array Indexing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('5th element on 2nd row: ', arr[1, 4])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# ? Count rows
print(arr[0, 1, 2])
# !Negative Indexing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Last element from 2nd dim: ', arr[1, -1])

# !Slicing arrays
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5:2])
# * 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
#! Data Types in Python
# By default Python have these data types:
'''
strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
'''
# ?Data Types in NumPy
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='S4')
print(arr)
print(arr.dtype)
# Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')
# !Converting Data Type on Existing Arrays
'''
The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
'''
new_arr = arr.astype('i8')
print(new_arr.dtype)
# !NumPy Array Copy vs View

'''
অনুলিপিটি ডেটার মালিক এবং অনুলিপিতে করা কোনও পরিবর্তন মূল অ্যারেকে প্রভাবিত করবে না এবং মূল অ্যারেতে করা কোনও পরিবর্তন অনুলিপিকে প্রভাবিত করবে না।

ভিউ ডেটার মালিক নয় এবং ভিউতে করা যেকোনো পরিবর্তন মূল অ্যারেকে প্রভাবিত করবে এবং মূল অ্যারেতে করা যেকোনো পরিবর্তন ভিউকে প্রভাবিত করবে।
'''

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

# * Base
'''
Every NumPy array has the attribute base that returns None if the array owns the data.
Otherwise, the base  attribute refers to the original object.
'''
print(x.base)  # None
print(y.base)  # Original object

# ! Shape of an Array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

'''
উপরের উদাহরণটি (2, 4) প্রদান করে, যার অর্থ হল অ্যারের 2টি মাত্রা রয়েছে, যেখানে প্রথম মাত্রাটিতে 2টি উপাদান রয়েছে এবং দ্বিতীয়টিতে 4টি রয়েছে।
'''
print(arr.shape)  # (first dimension, 2nd dimension)

# arr = np.array([1, 2, 3, 4], ndmin=5)
# [[[[[1 2 3 4]]]]]
# shape of array : (1, 1, 1, 1, 4)

# !NumPy Array Reshaping
# Reshaping means changing the shape of an array.
'''
here total element = rows * column
'''
arr = np.array(range(100))
newarr = arr.reshape(5, 5, 2, 2)
# reshape(first dimension, 2nd dimension, 3rd dimension)
# print(arr.reshape(2, 4).base) #The example above returns the original array, so it is a view.
# !Unknown Dimension
# ?can only specify one unknown dimension
# ?Pass -1 as the value, and NumPy will calculate this number for you.

newarr = arr.reshape(2, 2, -1)

# print(newarr)
# print(newarr.reshape(-1))
# !NumPy Array Iterating by for loop
# !Iterating Arrays Using nditer()

'''ফাংশনটি nditer()একটি সাহায্যকারী ফাংশন যা খুব মৌলিক থেকে খুব উন্নত পুনরাবৃত্তিতে ব্যবহার করা যেতে পারে। এটি কিছু মৌলিক সমস্যার সমাধান করে যা আমরা পুনরাবৃত্তিতে সম্মুখীন হই, উদাহরণ সহ এটির মধ্য দিয়ে যাওয়া যাক।

প্রতিটি স্কেলার এলিমেন্টে পুনরাবৃত্তি করা
মৌলিক লুপগুলিতে, একটি অ্যারের প্রতিটি স্কেলারের মাধ্যমে পুনরাবৃত্তি করার জন্য আমাদের nfor লুপ ব্যবহার করতে হবে যা খুব উচ্চ মাত্রার অ্যারের জন্য লেখা কঠিন হতে পারে। for

'''
for i in np.nditer(np.array(newarr)):
    # print(i)
    pass
'''
আমরা op_dtypesআর্গুমেন্ট ব্যবহার করতে পারি এবং পুনরাবৃত্তি করার সময় উপাদানগুলির ডেটাটাইপ পরিবর্তন করতে এটিকে প্রত্যাশিত ডেটাটাইপ পাস করতে পারি।

NumPy ইন-প্লেস এলিমেন্টের ডেটা টাইপ পরিবর্তন করে না (যেখানে এলিমেন্টটি অ্যারে আছে) তাই এই ক্রিয়াটি সম্পাদন করার জন্য এটির অন্য কিছু স্থান প্রয়োজন, সেই অতিরিক্ত স্থানটিকে বাফার বলা হয় এবং এটিকে সক্ষম করার জন্য আমরা পাস nditer()করি flags=['buffered']।
'''
for i in np.nditer(np.array(newarr), flags=["buffered"], op_dtypes=['S']):
    pass

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for x in np.nditer(arr[:, ::2]):
#     print(x)

# !ndenumerate() ব্যবহার করে গণনাকৃত পুনরাবৃত্তি
'''
কখনও কখনও আমাদের পুনরাবৃত্তি করার সময় উপাদানটির সংশ্লিষ্ট সূচকের প্রয়োজন হয়, ndenumerate()পদ্ধতিটি সেই ইউজকেসগুলির জন্য ব্যবহার করা যেতে পারে।
'''
# print(dict(np.ndenumerate(arr)))
# !Joining NumPy Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
# print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1, dtype='S')
# print(arr)
# !Joining Arrays Using Stack Functions
'''
স্ট্যাকিং কনক্যাটেনেশনের মতোই, একমাত্র পার্থক্য হল স্ট্যাকিং একটি নতুন অক্ষ বরাবর করা হয়।

আমরা দ্বিতীয় অক্ষ বরাবর দুটি 1-ডি অ্যারেকে সংযুক্ত করতে পারি যার ফলে তাদের একটিকে অন্যটির উপরে স্থাপন করা হবে, যেমন। স্ট্যাকিং

আমরা অ্যারেগুলির একটি ক্রম পাস করি যা আমরা stack()অক্ষ বরাবর পদ্ধতিতে যোগ দিতে চাই। যদি অক্ষ স্পষ্টভাবে পাস না হয় তবে এটি 0 হিসাবে নেওয়া হয়।
'''
# todo axis = 1

arr = np.stack((arr1, arr2), axis=1)
# print(arr)

# !সারি বরাবর স্ট্যাকিং
arr = np.hstack((arr1, arr2))
# print(arr)
# !কলাম বরাবর স্ট্যাকিং
arr = np.vstack((arr1, arr2))
# print(arr)
# !উচ্চতা বরাবর স্ট্যাকিং (গভীরতা)
arr = np.dstack((arr1, arr2))
# print(arr)
# !Splitting NumPy Arrays
'''
We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
'''
# arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
# print(newarr)
# !An alternate solution is using hsplit() opposite of hstack()
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])
newarr = np.hsplit(arr, 3)
# !Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().
newarr = np.vsplit(arr, 3)
# print(newarr)
#! Searching Arrays
'''
You can search an array for a certain value, and return the indexes that get a match.
'''
# To search an array, use the where() method.
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# # arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# x = np.where(arr%2 == 0)

# print(x)
#! Search Sorted
'''
searchsorted() নামে একটি পদ্ধতি রয়েছে যা অ্যারেতে একটি বাইনারি অনুসন্ধান করে এবং সূচী প্রদান করে যেখানে অনুসন্ধানের ক্রম বজায় রাখার জন্য নির্দিষ্ট মান সন্নিবেশ করা হবে।
Example explained: The number 7 should be inserted on index 1 to remain the sort order.
'''
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

# Search From the Right Side

x = np.searchsorted(arr, 7, side='right')
# Example explained: The number 7 should be inserted on index 2 to remain the sort order.
print(x)
# Multiple Values
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
#! Sorting Arrays
# The NumPy ndarray object has a function called sort(), that will sort a specified array.
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
# !NumPy Filter Array
'''
একটি বিদ্যমান অ্যারে থেকে কিছু উপাদান বের করা এবং তাদের থেকে একটি নতুন অ্যারে তৈরি করাকে ফিল্টারিং বলা হয় ।
'''

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
'''
উপরের উদাহরণে ফিরে আসবে [41, 43]কেন?

কারণ নতুন অ্যারেতে শুধুমাত্র সেই মান রয়েছে যেখানে ফিল্টার অ্যারের মান ছিল True, এই ক্ষেত্রে, সূচক 0 এবং 2।
'''
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(type(newarr))
# !অ্যারে থেকে সরাসরি ফিল্টার তৈরি করা
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
