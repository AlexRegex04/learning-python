from numpy import random
# # ?  3 rows, each row containing 5 random numbers:
x = random.choice([True, False], size=(100))
print(list(x).count(True))
