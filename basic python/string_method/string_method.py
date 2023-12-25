print('rakib'.capitalize())
print('RAKIB'.casefold())
txt = "banana"
x = txt.center(20)
print(x)

print('rakib'.count('a'))
print('rakib'.endswith('b'))
print('rakib'.startswith('r'))
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)

print('rakib'.find('k'))
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {:o}".format("John", 300006)
print(txt3)
print('rakib'.index('r'))


txt = '534'
x = txt.isdecimal()
print(x)

print('isidentifier')
print('5345'.isdigit())
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print('rakib'.islower())
print('56656'.isnumeric())
print('rakib'.isnumeric())
print('rakib'.isprintable())
print(' '.isspace())
print("RKAIB".isupper())

myDict = {"name": "John", "country": "Norway"}
mySeparator = "#"
x = mySeparator.join(myDict.values())
print(x)

txt = "banana"
x = txt.ljust(20, "O")
print(x)

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
print(txt.rfind('a'))
