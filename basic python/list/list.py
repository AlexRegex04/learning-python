fruits = ['apple', 'apple', 'banana', 'orange', 'apple', 'lemon']
#! Slicing
# print(fruits[3:])


# constructor => list()
#! Access item
# print(fruits[2])

# ! Change item
# fruits[1] = 'levu'
# print(fruits)

# ! range(include, not_include, step)
x = range(100, 200, 2)
# print(list(x))

# Argument vs parameter vs keyword

# !Add element
# fruits.append('levu')

# !Delete all element
# fruits.clear()
# del fruits[-1]
# print(fruits)
# ! Copy a list
# newFruitsList = fruits.copy()
# !Count Element
# print(fruits.count('apple2'))

# ! Extend list
# fruits.extend(list(range(10, 100)))
# print(fruits)

# !Find index (if could not find raise an error)
# print(fruits.index('apple', 2, 4))
# ! Insert an element
# fruits.insert(4, 'কলা')
# ! Remove an element specified position (pop(index))
# print(fruits)
# fruits.pop(0)
# print(fruits)
# ! Remove (if could not find raise an error)
# fruits.remove('lemon')
# Reverse()
# fruits = ['apple', 'banana', 'orange', 'lemon']
# fruits.reverse()
# print(fruits)

# Sorting
# x = [1, 5, 10, 11, 12]
# x.sort(reverse=False)


# Range
# x = range(10, 20, 4)
# print(list(x))
