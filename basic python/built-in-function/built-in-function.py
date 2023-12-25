from pprint import pprint
# print("abs:", abs(-20))
# print("all:", all(list(range(10))))
# print("any:", any(list(range(10))))
# print("Ascii", ascii("My name is Ståle"))
# print("bin:", bin(300))
# print("bool:", bool(0))
# print("bytearray:", bytearray(range(0, 256)))
# print("bytes:", bytes(tuple((196549,))))
# print("callable:", callable(len))
# print("chr:", chr(535))


# class Person:
#     name = "John"
#     age = 36
#     country = "Norway"

#     def __init__(self) -> None:
#         pass

#     def ff():
#         pass


# print("classmethod", classmethod(Person.ff()))
# print(divmod(10, 10))
# print(delattr(Person, 'age'))

# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)
# print((y))
# !format
# print(format(1000, '%'))
x = {"name": "rakib"}
# print(globals())

# print(id(x))
x = isinstance("Hello", (float, int, str, list, dict, tuple))
print(x)

x = isinstance(5, float)
print(x)

a = ("John", "Charles", "Mike",)
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
print(dict(enumerate(a)))
print(dict(x))
