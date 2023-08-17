import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Variables')
root.geometry('300x200')

# create a string variable
string_var = tk.StringVar() # int, double, boolean
 
def button_click_func():
    label.configure(text=string_var.get())
    button.configure(state='disabled')

entry = ttk.Entry(root, textvariable=string_var)
entry.pack()

button = ttk.Button(root, text='Click Me', command=button_click_func)
button.pack()

label = ttk.Label(root)
label.pack()

root.mainloop()