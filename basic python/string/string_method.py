
# print(x.capitalize())
# print(x.casefold())

# print(x.count('O'))
# print(x.endswith('M', 0, 8))  # !Boolean

# print(x.find('m')) # If couldn't find (-1)
# print(x.find("MO"))
# print(x.index('Mm')) # If couldn't find raise an error

# x = "I am {:%} years old"
# print(x.format(100))
# x = "1010"
# *print(x.isdecimal())
# !print(x.islower())
# !print(x.isnumeric())
# print(' '.isspace())

# print("Rakib".istitle())
# print("RAKIB".isupper())

# myDict = {"name": "John", "country": "Norway"}
# myList = ['My', "name", "Rakib"]

# mySeparator = " "
# x = mySeparator.join(myList)
# print(x)
x = 'man is man is Mortal'
# print(x.rjust(30, 'A'))
# print(x.rpartition('is'))
# y = x.split('m', 2)
# print(' '.join(y))
string = "MD RAKIBUL ISLAM"
print([*string])

lst = []
for letter in string:
    lst.append(letter)

letter = [x for x in string]

print(list(string))

lst = []
lst.extend(string)
print(lst)
