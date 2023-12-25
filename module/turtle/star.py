import turtle
import random
import math
t = turtle.Pen()


# for x in range(1,5):
#     t.forward(50)
#     t.left(90)
# # canvas reset করতে
# t.reset()

# for x in range(1,9):
#     t.forward(109)
#     t.left(225)

# t.reset()

# for x in range(1,100):
#     t.forward(300)
#     t.left(95)
# ***********************************************************
def mysquere(size):
    color = ['red', '#0B8F42', 'lime', '#0D8BF2','gold','#07F36C','#ff00a5','#1db1e8','#fb5304','#fe7b26']
    t.color(color[math.floor(random.random() * 10)])
    
    for x in range(0,4):
        t.forward(size)
        t.left(90)
t.reset()
mysquere(25)
mysquere(50)
mysquere(100)
mysquere(150)
mysquere(200)
mysquere(250)
mysquere(300)
t.right(90)
mysquere(25)
mysquere(50)
mysquere(100)
mysquere(150)
mysquere(200)
mysquere(250)
mysquere(300)
t.right(90)

mysquere(25)
mysquere(50)
mysquere(100)
mysquere(150)
mysquere(200)
mysquere(250)
mysquere(300)
t.right(90)

mysquere(25)
mysquere(50)
mysquere(100)
mysquere(150)
mysquere(200)
mysquere(250)
mysquere(300)
# ***********************************************************
