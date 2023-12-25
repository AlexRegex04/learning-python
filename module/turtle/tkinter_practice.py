import time
import os
from tkinter import *
import random


# * task:
# ^ 1. canvas move()
# ^ 1. time module
# ^ 1. random module
# ^ 1. PIL
# ^ 1. canvas move()
# ^ 1. canvas move()

root = Tk()
root.geometry("1000x1000")
root.configure(background="grey")
root.title("Canvas - Draw Shapes")

root.resizable(True, True)

canvas = Canvas(root, width=500, height=500)
canvas.pack(pady=20, padx=10)
# canvas.create_line(0, 0, 500, 500)

color = ['red', 'blue', 'gold', 'aqua', 'pink', 'green',
         'orange', 'yellow', 'purple', 'violet', 'magenta', 'cyan']


def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1+random.randrange(width))
    y2 = random.randrange(y1+random.randrange(height))
    canvas.create_rectangle(
        x1, y1, x2, y2, fill=color[random.randrange(0, len(color))])


def gen():
    for x in range(1, 1000):
        random_rectangle(width=x+100, height=x+100)


btn = Button(text='test', background='gold', command=gen)
btn.pack(padx=10)

x = canvas.create_polygon(10, 10, 10, 60, 50, 35)
y = canvas.create_rectangle(10, 10, 100,100)

print(x, y)

def movetriangle(event):
    print(event)
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)


for x in range(0, 100):
    canvas.move(1, 1, 3)
    root.update()
    time.sleep(0.05)
canvas.bind_all('<KeyPress>', movetriangle)
root.mainloop()
