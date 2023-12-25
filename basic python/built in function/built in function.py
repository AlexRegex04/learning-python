print('abs: ', abs(-100))
# Returns True if all items in an iterable object are true
print("all:", all(list(range(1, 100))))

# Returns True if any item in an iterable object is true
print("any:", any(list(range(0, 10))))

# The ascii() function will replace any non-ascii characters with escape characters:
# å will be replaced with \xe5.
print("Ascii", ascii("My name is Ståle"))
print(bin(10))
print(bool(0))
print(bytearray(9))
print(bytes(9))


def x():
    a = 5


print(callable(x))
print(chr(425))
print(complex(1, 10))


class Person:
    name = "John"
    age = 36
    country = "Norway"


print(getattr(Person, 'ages', 'test'))

delattr(Person, 'age')

x = dict(name="John", age=36, country="Norway")
print(x)
x = divmod(89, 3)  # *(29, 2)
print(x)

print(list(enumerate(tuple(range(0, 10)))))
x = 'print(55)'
eval(x)

ages = [5, 12, 18, 24, 32]


def myFunc(x):
    if (x > 18):
        return True
    else:
        return False


adults = filter(myFunc, ages)
print(list(adults))

print(format(90, '%'))
print(frozenset(['apple', 'banana', 'cherry']))
# x = globals()
# print(x)
# help()
print(id(adults))
# ************************************
x = isinstance(5, float)
x = isinstance("Hello", (float, int, str, list, dict, tuple))


class myObj:
    name = "John"


y = myObj()
x = isinstance(y, myObj)
print(x)


class myAge:
    age = 36


class myObj(myAge):
    name = "John"
    age = myAge


x = issubclass(myObj, myAge)

x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

# **********************
# x  = locals()
# print(x)


def myfunc(n):
    return len(n)


x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))

print(list(memoryview(bytes(ages))))

print()
x = ord('h')
print(x)

x = pow(4, 3, 5)
print(x)

alph = ["a", "b", "c", "d"]
ralph = reversed(alph)


x = round(5.76543, 2)
print(x)


class Person:
    name = "John"
    age = 36
    country = "Norway"


setattr(Person, 'f', 40)
print(Person.f)

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a, reverse=True)
print(x)


class Person:
    name = "John"
    age = 36
    country = "norway"


x = vars(Person)
a = ("John", "Charles", "Mike",)
b = ("Jenny", "Christy", "Monica")
c = tuple(range(0, 10))

x = zip(a, b, c)

print(list(x))
