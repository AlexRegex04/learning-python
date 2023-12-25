txt = "The best things in life are free!"
# check
print('The' in txt)
print("The" not in txt)
# Slicing
print(txt[0:1])
print(txt[4:])
print(txt[:4])
# python format
x = "my name is {}"
print(x.format('rakib'))
x = "my name is {0}. I am {1} years old"
print(x.format('rakib', 200))
x = "my name is {name}. I am {age} years old"
print(x.format(age=10, name='rakib'))

# Old version
# String (%s)
# Integer (%i)
# Float (%f)
# Double (%d)

# Character(%c) => int or char
name = "Rakib"
age = 11000
print("Hello, %s. You are %o." % (name, age))

# Best for practice
print(f'I am {name} . I am {age} old')

# Python escape character
x = 'I\'m rakib'
print(x)

a = {'a': 1, "b": 2}
b = {"c": 3, "d": 4}

print({**a, **b})
