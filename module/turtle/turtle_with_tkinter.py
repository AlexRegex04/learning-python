# from tkinter import *
# tk = Tk()
# import turtle
# import random
# import math


# def hello():
#     t = turtle.Pen()
#     for x in range(1,100):
#         t.forward(300)
#         t.left(95)
# def check():
#     t = turtle.Pen()
#     for x in range(1,100):
#         t.forward(109)
#         t.left(225)

# btn = Button(tk, text='click me', command=hello)
# btn.pack()
# btn1 = Button(tk, text='click me', command=check)
# btn1.pack()
# tk.mainloop()


# from tkinter import ttk
# from tkinter.messagebox import showerror

# root = tk.Tk()
# root.title('Temperature Converter')
# root.geometry('300x70')
# root.resizable(False, False)

# def fahrenheit_to_celsius(f):
#     """ Convert fahrenheit to celsius
#     """
#     return (f - 32) * 5/9

# frame = ttk.Frame(root)
# options = {'padx': 5, 'pady': 5}

# # temperature label
# temperature_label = ttk.Label(frame, text='Fahrenheit')
# temperature_label.grid(column=0, row=0, sticky='W', **options)
# # temperature entry
# temperature_entry = ttk.Entry(frame, textvariable="temperature")
# temperature_entry.grid(column=1, row=0, **options)
# temperature_entry.focus()

# # convert button
# convert_button = ttk.Button(frame, text='Convert')
# convert_button.grid(column=2, row=0, sticky='W', **options)
# # convert_button.configure(command=convert_button_clicked)
# # result label
# result_label = ttk.Label(frame)
# result_label.grid(row=1, columnspan=3, **options)
# frame.grid(padx=10, pady=10)
# root.mainloop()
