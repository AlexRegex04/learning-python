# x = 100
# def test():
#     global y
#     y = 400
#     pass
# test()
from pprint import pprint as print
# print(y)

x = {
    "brand": "Ford",
    "electric": False,
    "colors": ["red", "white", "blue"],
}

# !length:
# print(len(x))
# !access item from dictionary
# print(x["colors"])
# ! change value
x["brand"] = "Volvo"
# ! Add value
x["age"] = 1964

#! method of dictionary
#! Clear all element
# print(x.clear())
# fromkeys
# x = dict.fromkeys(tuple(('age',)), 1000)
# print(x)
# ! get a specific item
x.get()
