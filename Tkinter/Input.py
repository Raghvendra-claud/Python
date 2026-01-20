# import Tkinter
import tkinter as tk

# creating window
root = tk.Tk()

# taking user input
e = tk.Entry()
e.insert(0,"Enter your name:")
'''
other parametres:
width, fg, bg, borderwidth

using get() function to display user input
using insert() function to display default text inside input box
'''
e.pack()

def myclick():
    hello = "Hello! "+e.get()
    mylabel = tk.Label(root, text=hello)
    mylabel.pack()

button = tk.Button(root,text="Click me!", command=myclick, fg="blue", background="red")

button.pack()

root.mainloop()