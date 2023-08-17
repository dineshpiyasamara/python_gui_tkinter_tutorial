import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Buttons')
root.geometry('300x200')

my_variable = tk.StringVar(value='Click Me')
number1 = tk.IntVar()
number2 = tk.IntVar()
sum_of_numbers = tk.StringVar()

def button_func(input1, input2):
    sum = input1.get() + input2.get()
    sum_of_numbers.set(sum)

get_number1 = ttk.Entry(root, textvariable=number1)
get_number2 = ttk.Entry(root, textvariable=number2)
get_number1.pack()
get_number2.pack()

button = ttk.Button(root, command=lambda: button_func(number1, number2), textvariable=my_variable)
button.pack()

label = ttk.Label(root, textvariable=sum_of_numbers)
label.pack()

root.mainloop()