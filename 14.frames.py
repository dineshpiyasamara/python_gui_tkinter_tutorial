import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Frames")
root.geometry("500x400")


####################
# frame = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
# frame.pack()

####################
# frame = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
# frame.pack_propagate(False)
# frame.pack()

# label1 = ttk.Label(frame, text="Hello")
# label1.pack()

####################
# frame = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
# frame.pack_propagate(False)
# frame.pack()

# label1 = ttk.Label(frame, text="Hello")
# label1.pack()

# label2 = ttk.Label(root, text="Welcome")
# label2.pack()

####################
frame = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')

entry = ttk.Entry(frame)
entry.pack(pady=10)

button = ttk.Button(frame, text='Submit')
button.pack()

label2 = ttk.Label(root, text="Welcome")
label2.pack()


root.mainloop()