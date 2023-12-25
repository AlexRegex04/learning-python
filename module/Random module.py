import math
import time
import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print("Random number: ", random_number)

# Save the current state of the random number generator
saved_state = random.getstate()

# Generate another random number
random_number = random.randint(1, 100)
print("Random number: ", random_number)

# Restore the previous state of the random number generator
random.setstate(saved_state)

# Generate another random number
random_number = random.randint(1, 100)
print("Random number: ", random_number)

print(random.getrandbits(2))
print(random.randrange(10, 100))
print(random.randint(a=10, b=34))
x = list(('rakib', 'rak', 'rani'))
print(random.shuffle(x))
print(random.choice(x))
print(random.sample(range(0, 10), 3))
print(random.random()*10)
print(random.uniform(10, 100))
print(random.triangular(10, 100, 10))

print(random.betavariate(20, 20))
print(random.expovariate(10))
print(random.gauss(math.pi))
print(random.lognormvariate(10, 00))


def outer_div(func):
    def inner(x, y):
        if (x < y):
           x, y = y, x
           return func(x,y)  
        return inner  
# syntax of generator  
@outer_div  
def divide(x,y):  
     print(x/y)  
