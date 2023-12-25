import turtle
import random
import math

# !map bangladesh
'''
for create a canvas 
automatic create a canvas
'''
t = turtle.Pen()



# t.forward(100)
color = ['red', '#0B8F42', 'lime', '#0D8BF2','gold','#07F36C','#ff00a5','#1db1e8','#fb5304','#fe7b26']
x = list(range(1, 1000, 5))
for y in x:
    t.color(color[math.floor(random.random() * 10)])
    t.up()
    t.down()
    t.right(45)
    # t.begin_fill()
    t.circle(y, 180,10)
    # t.end_fill()
    t.left(90)

# for y in x:
#     t.color(color[math.floor(random.random() * 10)])
#     t.backward(y)
#     t.up()
#     t.down()
#     t.circle(10, 300)
#     t.backward(y)
#     t.left(90)
